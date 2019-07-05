TILES = ('-', ' ', '-', ' ', '-', '||',
         '_', '|', '_', '|', '_', '|', '||',
         '&', ' ', '_', ' ', '||',
         ' ', ' ', ' ', '^', ' ', '||'
)

for cell in TILES:
    line_end = ""
    tile = "{}"
    if cell == "||":
        output = tile.format("")
        line_end = "\n"
    else :
        output = tile.format(cell)
    print(output, end = line_end)