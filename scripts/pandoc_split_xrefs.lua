-- Split cross-reference notes (X:) from regular footnotes.
-- Xrefs become \CrossRefNote in a separate LaTeX footnote stream.
-- The printed xref table is keyed by the current verse number.

local function tex_escape(s)
  s = s:gsub("\\", "\\textbackslash{}")
  s = s:gsub("([{}#%$%%&_])", "\\%1")
  s = s:gsub("~", "\\textasciitilde{}")
  s = s:gsub("%^", "\\textasciicircum{}")
  return s
end

local function xref_text(elem)
  local content = pandoc.utils.stringify(elem.content)
  local trimmed = content:gsub("^%s+", "")
  if trimmed:match("^X:") then
    return trimmed:gsub("^X:%s*", "")
  end
  return nil
end

local function verse_number(elem)
  if elem.t ~= "Strong" then
    return nil
  end
  local text = pandoc.utils.stringify(elem.content):gsub("%s+", "")
  if text:match("^%d+$") then
    return text
  end
  return nil
end

function Inlines(inlines)
  local current_verse = nil
  local output = pandoc.List()

  for _, inline in ipairs(inlines) do
    local verse = verse_number(inline)
    if verse then
      current_verse = verse
    end

    if inline.t == "Note" then
      local xref = xref_text(inline)
      if xref then
        local label = current_verse or "?"
        output:insert(
          pandoc.RawInline(
            "latex",
            "\\CrossRefNote{" .. tex_escape(label) .. "}{" .. tex_escape(xref) .. "}"
          )
        )
      else
        output:insert(inline)
      end
    else
      output:insert(inline)
    end
  end

  return output
end
