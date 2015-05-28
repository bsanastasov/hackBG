class Fractions:

	def __init__(self, num, denum):
		self.num = num
		self.denum = denum

	def __str__(self):
		message = "({} / {})".format(self.num, self.denum)
		return message

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other):
		return self.num / self.denum == other.num / other.denum

	def __add__(self, other):
		num = self.num * other.num + self.denum * other.num
		denum = self.denum * other.denum
		return Fractions(num, denum)

	def __mul__(self, other):
		num = self.num * other.num
		denum = self.denum * other.denum
		return Fractions(num, denum)

	def __truediv__(self, other):
		num = self.num * other.denum
		denum = self.denum * other.num
		return Fractions(num, denum)

	def __sub__(self, other):
		num = self.num * other.denum - self.denum * other.num
		denum = self.denum * other denum
		return Fractions(num, denum)




