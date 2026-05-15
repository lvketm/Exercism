def response(hey_bob):
    def question(string):
        if string.strip().endswith("?"):
            return True
        else:
            return False
    
    def yelling(string):
        has_letters = any(letter.isalpha() for letter in string)
        if has_letters and all(letter.isupper() for letter in string if letter.isalpha()):
            return True
        else:
            return False
    
    def silence(string):
        if string.strip() == "":
            return True
        else:
            return False

    if silence(hey_bob):
        return "Fine. Be that way!"
    elif question(hey_bob) and yelling(hey_bob):
        return "Calm down, I know what I'm doing!"
    elif question(hey_bob):
        return "Sure."
    elif yelling(hey_bob):
        return "Whoa, chill out!"
    else:
        return "Whatever."
    
