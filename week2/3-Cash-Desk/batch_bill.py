from bill import Bill

class BatchBill(Bill):
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