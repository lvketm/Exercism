def steps(number):
    cout = 0
    if not str(number).isnumeric() or number == 0:
        raise ValueError("Only positive integers are allowed")
    while number != 1:
        if number % 2 == 0:
            number /= 2
            cout += 1
        else:
            number = number * 3 + 1
            cout += 1
    return cout
