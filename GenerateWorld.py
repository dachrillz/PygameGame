def ConvertAsciiToTile(tilemap):
#[ '#', '?', '%', '.', 'S', '+', '.', '*', ':', ',', '@']
    for i in range(len(tilemap)):
        for j in range(len(tilemap[i])):
            tilemap[i][j] = 1
            
    return tilemap