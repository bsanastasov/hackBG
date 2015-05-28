class Bill:

	def __init__(self,amount):
		self.amount = amount

	def __str__(self):
		return "A {} is a bill".format(self.amount)

	def __repr__(self):
		return self.__str__()

	def __int__(self):
		return self.amount

	def __eq__(self, other):
		return self.amount == other.amount

	def __hash__(self):
		return hash(self.amount)

class BachBill(Bill):
	def __init__(self,bills):
		self.bills = bills

	def __len__(self):
		return len(self.bills)

	def total(self):
		sum = 0
		for bill in self.bills:
			sum += int(bill)
		return sum

	def __getitem__(self, index):
		return self.bills[index]

	def __int__(self):
		return self.total()

class CashDesk:
	def __init__(self):
		self.money = []

	def take_money(self, currency):
		self.money.append(currency)

	def total(self):
		result = 0
		for money in self.money:
			result += int(money)
		return result

	def inspect(self):

