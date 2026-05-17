local heading_path = "data/research/print_pericope_headings.csv"
local headings = {}

local function parse_csv_line(line)
  local fields = {}
  local field = {}
  local quoted = false
  local index = 1
  while index <= #line do
    local char = line:sub(index, index)
    if char == '"' then
      if quoted and line:sub(index + 1, index + 1) == '"' then
        table.insert(field, '"')
        index = index + 1
      else
        quoted = not quoted
      end
    elseif char == "," and not quoted then
      table.insert(fields, table.concat(field))
      field = {}
    else
      table.insert(field, char)
    end
    index = index + 1
  end
  table.insert(fields, table.concat(field))
  return fields
end

local function load_headings()
  local handle = io.open(heading_path, "r")
  if handle == nil then
    return
  end
  local header_seen = false
  for line in handle:lines() do
    if not header_seen then
      header_seen = true
    else
      local fields = parse_csv_line(line)
      local heading = fields[2] or ""
      local status = (fields[4] or "active"):lower()
      if heading ~= "" and (status == "" or status == "active") then
        headings[heading] = true
      end
    end
  end
  handle:close()
end

local function latex_escape(text)
  text = text:gsub("\\", "\\textbackslash{}")
  text = text:gsub("([%%$#&_{}])", "\\%1")
  text = text:gsub("~", "\\textasciitilde{}")
  text = text:gsub("%^", "\\textasciicircum{}")
  return text
end

load_headings()

function Para(element)
  local text = pandoc.utils.stringify(element)
  if headings[text] then
    return pandoc.RawBlock(
      "latex",
      "\\subsubsection*{" .. latex_escape(text) .. "}"
    )
  end
  return nil
end
