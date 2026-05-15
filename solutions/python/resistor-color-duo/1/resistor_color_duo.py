color_map = {
            'black': 0,
            'brown': 1,
            'red': 2, 
            'orange': 3,
            'yellow': 4,
            'green': 5,
            'blue': 6,
            'violet': 7,
            'grey': 8,
            'white': 9,
        }

def value(colors):
    band_value = ""
    i = 0
    while i < 2:
        band_value += str(color_map[f"{colors[i]}"])
        i += 1
    return int(band_value)
