-- Emit native LaTeX running-header marks and red verse numbers for print PDFs.
-- This runs after xref splitting so cross-reference note association still sees
-- the original Strong verse markers.

local function latex_escape(text)
  text = text:gsub("\\", "\\textbackslash{}")
  text = text:gsub("([%%$#&_{}])", "\\%1")
  text = text:gsub("~", "\\textasciitilde{}")
  text = text:gsub("%^", "\\textasciicircum{}")
  return text
end

local function compact_text(inlines)
  return pandoc.utils.stringify(inlines):gsub("^%s+", ""):gsub("%s+$", "")
end

local function verse_marker_filter(book, chapter)
  return function(element)
    local verse = compact_text(element.content)
    if not verse:match("^%d+$") then
      return nil
    end

    return pandoc.RawInline(
      "latex",
      "\\GHSBVerse{"
        .. latex_escape(book)
        .. "}{"
        .. latex_escape(chapter)
        .. "}{"
        .. latex_escape(verse)
        .. "}{"
        .. latex_escape(verse)
        .. "}"
    )
  end
end

function Pandoc(doc)
  local current_book = nil
  local current_chapter = nil
  local blocks = {}

  for _, block in ipairs(doc.blocks) do
    if block.t == "Header" then
      local text = compact_text(block.content)
      if block.level == 1 then
        current_book = text
        current_chapter = nil
        table.insert(blocks, block)
      elseif block.level == 2 then
        local chapter = text:match("^Chapter%s+(%d+)$")
        if chapter then
          current_chapter = chapter
          table.insert(
            blocks,
            pandoc.RawBlock(
              "latex",
              "\\subsection{\\textcolor{GHSBRed}{" .. latex_escape(text) .. "}}"
            )
          )
        else
          current_chapter = nil
          table.insert(blocks, block)
        end
      else
        table.insert(blocks, block)
      end
    elseif current_book ~= nil and current_chapter ~= nil then
      table.insert(
        blocks,
        pandoc.walk_block(block, { Strong = verse_marker_filter(current_book, current_chapter) })
      )
    else
      table.insert(blocks, block)
    end
  end

  doc.blocks = blocks
  return doc
end
