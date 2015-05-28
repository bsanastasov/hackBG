from bill import Bill
from batch_bill import BatchBill

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

