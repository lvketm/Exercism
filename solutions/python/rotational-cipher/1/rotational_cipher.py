def rotate(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            # Determine ASCII base
            base = ord('A') if char.isupper() else ord('a')

            # Shift character
            shifted = (ord(char) - base + shift) % 26 + base

            result += chr(shifted)
        else:
            # Keep spaces, punctuation, numbers unchanged
            result += char

    return result


