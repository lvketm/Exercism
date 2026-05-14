def equilateral(sides):
	if check_if_valid(sides):
		if sides[0] == sides[1] == sides[2]:
			return True
		else:
			return False
	return False


def isosceles(sides):
	if check_if_valid(sides):
		if sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]:
			return True
		else:
			return False
	return False


def scalene(sides):
	if check_if_valid(sides):
		if sides[0] != sides[1] and sides[1] != sides[2] and sides[0] != sides[2]:
			return True
		else:
			return False
	return False

def check_if_valid(sides):
		a = sides[0]
		b = sides[1]
		c = sides[2]
		
		if a <= 0 or b <= 0 or c <= 0:
			return False

		if a + b >= c and b + c >= a and a + c >= b:
			return True
		else:
			return False

