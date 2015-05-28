def factorial(n):
	faktN = 1
	for i in range(1,n+1):
		faktN*=i
	return faktN
	

def fibonacci(n):
	prev=0
	next=1
	sum=0
	for i in range(0,n+1):
		print prev,
		sum=prev+next
		prev=next
		next=sum

def sum_digits(n):
    return sum(to_digits(n))


def fact_digits(n):
    s = 0
    while n:
		s = n % 10
		n /= 10
		m = 1
		for i in range(1,s+1):
			m *= i
		return m


def palindrome(a):
     return str(a) == str(a)[::-1] 


def to_digits(n):
	return [int(x) for x in str(n)]


def magic(numList):        
    s = ''.join(map(str, numList))
    return int(s) 



def to_number(digits):
    result = 0

    for digit in digits:
        digits_count = count_digits(digit)
        result = result * (10 ** digits_count) + digit

    return result


def fibonacci_number(n):
    return to_number(fibonacci(n))


 def count_vowels(str):
    num_vowels=0
    for char in str:
        if char in "aeiouAEIOU":
           num_vowels +=1
    return num_vowels


def count_consonants(str):
    num_consonants=0
    for char in str:
        if not char in "aeiouAEIOU":
           num_consonants +=1
    return num_consonants
print count_consonants('Pythonmaina')


def char_histogram(string):
    result = {}

    for ch in string:
        if ch in result:
            result[ch] += 1
        else:
            result[ch] = 1

    return result


def p_score(n):
    if palindrome(n):
        return 1

    s = n + int(str(n)[::-1])

    return 1 + p_score(s)


def even(n):
    return n % 2 == 0


def odd(n):
    return not even(n)


def is_hack(n):
    binary_n = bin(n)[2:]

    is_palindrome = palindrome(binary_n)
    has_odd_ones = odd(binary_n.count("1"))

    return is_palindrome and has_odd_ones


def next_hack(n):
    n += 1

    while not is_hack(n):
        n += 1

    return n


