def convert(number):
    suffix = ""

    if number % 3 == 0:
        suffix += "Pling"
    if number % 5 == 0:
        suffix += "Plang"
    if number % 7 == 0:
        suffix += "Plong"

    if suffix != "":
        return suffix
    else:
        return str(number)
