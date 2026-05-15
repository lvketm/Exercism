def classify(number):
    def aliquot_sum(number):
        sum = 0
        aliquots = []

        for i in range(1, number):
            if number % i == 0:
                aliquots.append(i)
        
        for i in range(len(aliquots)):
            sum += aliquots[i]
        
        return sum


    if number < 1 or not str(number).isnumeric():
        raise ValueError("Classification is only possible for positive integers.")
    elif aliquot_sum(number) == number:
        return "perfect"
    elif aliquot_sum(number) > number:
        return "abundant"
    else:
        return "deficient"
