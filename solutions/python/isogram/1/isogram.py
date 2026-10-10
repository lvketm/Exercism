def is_isogram(phrase):
    letters = []
    for i in range(len(phrase)):
        char = phrase[i].lower()
        if char.isalpha() and char not in letters:
            letters.append(char)
        elif char.isalpha():
            return False
    return True
