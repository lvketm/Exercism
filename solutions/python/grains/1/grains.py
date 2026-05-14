def square(number):
	if verify_validity(number):
    		return 2 ** (number - 1)


def total():
	return 2 ** 64 - 1
		

def verify_validity(number):
	if number <= 0 or number > 64:
		raise ValueError("square must be between 1 and 64")
	else:
		return True
