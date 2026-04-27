"""Disk cache helpers for deterministic ingest steps."""

from __future__ import annotations

import hashlib
import json
import os
import pickle
from collections.abc import Callable, Iterable
from pathlib import Path
from typing import TypeVar


T = TypeVar("T")


def cache_enabled(env_name: str) -> bool:
    value = os.environ.get(env_name, "").strip().casefold()
    return value not in {"1", "true", "yes", "on"}


def relative_path(path: Path, root: Path) -> str:
    try:
        return path.resolve().relative_to(root).as_posix()
    except ValueError:
        return path.as_posix()


def file_fingerprint(path: Path, root: Path) -> dict[str, object]:
    if not path.exists():
        return {
            "path": relative_path(path, root),
            "exists": False,
            "size": None,
            "mtime_ns": None,
        }
    stat = path.stat()
    return {
        "path": relative_path(path, root),
        "exists": True,
        "size": stat.st_size,
        "mtime_ns": stat.st_mtime_ns,
    }


def cache_key(
    *,
    version: str,
    label: str,
    dependencies: Iterable[Path],
    params: dict[str, object],
    root: Path,
) -> str:
    payload = {
        "version": version,
        "label": label,
        "params": params,
        "dependencies": [file_fingerprint(path, root) for path in dependencies],
    }
    return hashlib.sha256(json.dumps(payload, sort_keys=True).encode("utf-8")).hexdigest()


def cached_result(
    *,
    label: str,
    dependencies: Iterable[Path],
    params: dict[str, object],
    producer: Callable[[], T],
    cache_dir: Path,
    root: Path,
    version: str,
    disable_env: str,
) -> tuple[T, dict[str, object]]:
    enabled = cache_enabled(disable_env)
    diagnostics: dict[str, object] = {
        "enabled": enabled,
        "version": version,
    }
    if not enabled:
        return producer(), diagnostics

    key = cache_key(version=version, label=label, dependencies=dependencies, params=params, root=root)
    cache_path = cache_dir / f"{label}-{key}.pickle"
    diagnostics.update(
        {
            "key": key[:16],
            "path": relative_path(cache_path, root),
            "hit": False,
        }
    )
    if cache_path.exists():
        try:
            with cache_path.open("rb") as handle:
                return pickle.load(handle), {**diagnostics, "hit": True}
        except Exception as exc:
            diagnostics["read_error"] = f"{type(exc).__name__}: {exc}"

    result = producer()
    try:
        cache_dir.mkdir(parents=True, exist_ok=True)
        tmp_path = cache_path.with_suffix(cache_path.suffix + ".tmp")
        with tmp_path.open("wb") as handle:
            pickle.dump(result, handle, protocol=pickle.HIGHEST_PROTOCOL)
        os.replace(tmp_path, cache_path)
        diagnostics["written"] = True
    except Exception as exc:
        diagnostics["write_error"] = f"{type(exc).__name__}: {exc}"
    return result, diagnostics
