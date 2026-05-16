def square_of_sum(number):
    return (number * (number + 1) / 2) ** 2


def sum_of_squares(number):
    numbers = 0

    for i in range(1, number + 1):
        numbers += i ** 2
    return numbers


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)


