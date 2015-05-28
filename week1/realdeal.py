def sum_of_divisors(n):
	divisors = []

	for i in range(1, n+1):
		if n%i == 0:
			divisors.append(i)

	return sum(divisors)

print (sum_of_divisors(1000))


def is_prime(n):
	if n<0:
		return False

	for i in range(1, n+1):
		if n%i==0 and (i!=1 and i!=n):
			return False
	
	return True

print (is_prime(-10))


def prime_number_of_divisors(n):
	divisors=[]

	for i in range(1, n+1):
		if n%i == 0:
			divisors.append(i)

	return is_prime(len(divisors))

print (prime_number_of_divisors(9))


def contains_digit(number, digit):
	if str(digit) in str(number):
		return True

	return False

print (contains_digit(12346789, 5))


def contains_digits(number, digits):
	for digit in digits:
		if str(digit) not in str(number):
			return False

	return True

print (contains_digits(456, []))

def number_to_list(n):
	digits = []
	n = str(n)

	for ch in n:
		digits.append(int(ch))

	return digits

print (number_to_list(123))

def balanced_number_sums(digits):
	sum1=0
	sum2=0

	for i in range(0, (len(digits)//2)):
			sum1 += digits[i]

	for i in range(len(digits)//2, len(digits)):
			sum2 += digits[i]

	if sum1 == sum2:
			return True

	return False


def is_number_balanced(n):
	by_digits = number_to_list(n)

	if len(by_digits)== 1:
		return True

	elif len(by_digits)%2 == 0:
		return balanced_number_sums(by_digits)

	else:
		by_digits.remove(by_digits[len(by_digits)//2])

		return balanced_number_sums(by_digits)

print (is_number_balanced(1238033))


def count_substrings(haystack, needle):
	return haystack.count(needle)

print (count_substrings("babababa", "baba"))


def count_digits(n):
	return sum([1 for x in number_to_list(n)])


def to_number(digits):
	result = 0
	for digit in digits:
		digits_count = count_digits(digit)
		result = result * (10 ** digits_count) + digit
	return result


def zero_insert(n):
	by_digits = number_to_list(n)
	result = []

	if len(by_digits) == 1:
		return by_digits

	for i in range(0, len(by_digits)-1):
		result.append(by_digits[i])

		if by_digits[i]==by_digits[i+1] or (by_digits[i]+by_digits[i+1])%10==0:
			result.append(0)

	result.append(by_digits[len(by_digits)-1])

	return to_number(result)

print (zero_insert(6446))


def sum_matrix(m):
	total = 0

	for row in m:
		total += sum(row)

	return total

print (sum_matrix([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]))


def check_corners(m, coords):
	x=coords[0]
	y=coords[1]

	if (x == 0 and y==0) or (x==0 and y==len(m[0])-1) or (x==len(m)-1 and y==0) or (x==len(m)-1 and y==len(m[0])-1):
		return True

	return False



def check_middle(m, coords):
	x=coords[0]
	y=coords[1]

	if x!=0 and y!=0 and x!=len(m)-1 and y!=len(m[0])-1:
		return True

	return False



def null_negatives(m):
	for i in range(0, len(m)):
		for j in range(0, len(m[i])):
			if m[i][j] < 0:
				m[i][j] = 0

	return m


def bomb_corners(m, coords):
	x=coords[0]
	y=coords[1]

	a=m[x][y]

	if x==y==0:
		m[x][y+1] -= a
		m[x+1][y] -= a
		m[x+1][y+1] -= a
	elif x==0 and y != 0:
		m[x][y-1] -= a
		m[x+1][y-1] -= a
		m[x+1][y] -= a
	elif x != 0 and y == 0:
		m[x-1][y] -= a
		m[x-1][y+1] -= a
		m[x][y+1] -= a
	elif x == len(m)-1 and y==len(m[0])-1:
		m[x-1][y-1] -= a
		m[x-1][y] -= a
		m[x][y-1] -= a

	m=null_negatives(m)
	return m


def bomb_edges(m, coords):
	x=coords[0]
	y=coords[1]

	a=m[x][y]

	if x == len(m)-1:
		m[x-1][y-1] -= a
		m[x][y-1] -= a
		m[x-1][y] -= a
		m[x-1][y+1] -= a
		m[x][y+1] -= a
	elif y == len(m[0])-1:
		m[x-1][y] -= a
		m[x-1][y-1] -=a
		m[x][y-1] -= a
		m[x+1][y-1] -= a
		m[x+1][y] -= a
	elif x == 0:
		m[x][y-1] -= a
		m[x+1][y-1] -= a
		m[x+1][y] -= a
		m[x+1][y+1] -= a
		m[x][y+1] -= a
	elif y == 0:
		m[x-1][y] -= a
		m[x-1][y+1] -= a
		m[x][y+1] -= a
		m[x+1][y+1] -= a
		m[x+1][y-1] -= a

	m=null_negatives(m)
	return m


def bomb_middle(m, coords):
	x=coords[0]
	y=coords[1]

	a=m[x][y]

	m[x-1][y-1] -= a
	m[x-1][y] -= a
	m[x-1][y+1] -= a
	m[x][y+1] -= a
	m[x+1][y+1] -= a
	m[x+1][y] -= a
	m[x+1][y-1] -= a
	m[x][y-1] -= a

	m=null_negatives(m)
	return m


def matrix_bombing_plan(m):
	result = {}

	import copy


	for i in range(0, len(m)):
		for j in range(0, len(m[i])):
			matrix_copy = copy.deepcopy(m)

			if check_corners(matrix_copy, (i, j)):
				result[(i, j)] = sum_matrix(bomb_corners(matrix_copy, (i, j)))	
			elif check_middle(matrix_copy, (i, j)):
				result[(i, j)] = sum_matrix(bomb_middle(matrix_copy, (i, j)))
			else:
				result[(i, j)] = sum_matrix(bomb_edges(matrix_copy, (i, j)))

	return result

print (matrix_bombing_plan([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
