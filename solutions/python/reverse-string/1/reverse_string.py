def reverse(text):
    reversed_text = ""
    for i in range(len(text)):
        reversed_text += text[-i - 1]
    return reversed_text

print(reverse("strops"))
