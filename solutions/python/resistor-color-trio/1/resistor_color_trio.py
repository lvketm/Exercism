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

def label(colors):
    # convert colors to values
    band_value = ""
    i = 0
    while i < len(colors) - 1:
        if color_map[colors[i]] == 0:
            i += 1
        else:
            band_value += str(color_map[colors[i]])
            i += 1
    
    # determine the final value
    value = (
        int(str(color_map[colors[0]]) + str(color_map[colors[1]]))
        * 10 ** color_map[colors[2]]
    )
    # return the full label
    if value >= 1_000_000_000:
        return f"{value // 1_000_000_000} gigaohms"
    elif value >= 1_000_000:
        return f"{value // 1_000_000} megaohms"
    elif value >= 1_000:
        return f"{value // 1_000} kiloohms"
    else:
        return f"{value} ohms"
