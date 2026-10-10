def is_pangram(sentence):
    letters = []
    for i in range(len(sentence)):
        char = sentence.lower()[i]
        if char.isalpha() and char not in letters:
            letters.append(char)
    return len(letters) == 26
