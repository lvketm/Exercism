def resistor_label(colors):
    color_map = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9,
    }

    tolerance = {
        "brown": 1,
        "red": 2,
        "green": 0.5,
        "blue": 0.25,
        "violet": 0.1,
        "grey": 0.05,
        "silver": 10,
        "gold": 5,
    }

    # a single black band is 0 ohms:
    if len(colors) == 1:
        return "0 ohms"

    # 4 bands: 2 digits, 5 bands: 3 digits
    digit_count = 2 if len(colors) == 4 else 3
    digits = colors[:digit_count]
    multiplier = colors[digit_count]
    tolerance = tolerance[colors[digit_count + 1]]

    number = int("".join(str(color_map[c]) for c in digits))
    value = number * 10 ** color_map[multiplier]

    # return the full label
    if value >= 1_000_000_000:
        return f"{value / 1_000_000_000:g} gigaohms ±{tolerance}%"
    elif value >= 1_000_000:
        return f"{value / 1_000_000:g} megaohms ±{tolerance}%"
    elif value >= 1_000:
        return f"{value / 1_000:g} kiloohms ±{tolerance}%"
    return f"{value} ohms ±{tolerance}%"