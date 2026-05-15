def score(x, y):
    distance = x ** 2 + y ** 2
    
    # inner circle 
    if distance <= 1:
        return 10
    # middle circle 
    elif distance <= 25:
        return 5
    # outer circle 
    elif distance <= 100:
        return 1
    # outside
    else:
        return 0
