from batch_bill import BatchBill
from bill import Bill
import unittest


class TestBatchBill(unittest.TestCase):
	def setUP(self):
		self.values = [10, 20, 50, 100]
		self.bills = [Bill(value) for value in self.values]
	def test_init(self):
		values = [10, 20, 50, 100]
		bills = [Bill(value) for value in values]

		my_batch = BatchBill()

		self.assertTrue(isistance(my_batch, Batchbill))
		self.assertEqual(my_batch.bills, bills)

	def test_irretation(self):
		self.assertEqual(self.my_batch[1], self.bills[1])


if __name__ == 'main':
	unittest.main()