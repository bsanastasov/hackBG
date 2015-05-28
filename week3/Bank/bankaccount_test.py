import unittest
from bankaccount import BankAccount

class BankAccountTest(unittest.TestCase):

    def setUp(self):
        self.set_account = BankAccount("Rado",500,"$")

    def test_init(self):
        self.assertTrue(isinstance(self.set_account, BankAccount))

    def test_str(self):
        my_account = BankAccount("Rado", 500, "$")
        needed_result = "Bank acccount for Rado with balance of 500 $"
        self.assertEqual(str(my_account), needed_result)

    def test_deposite(self):
        self.my_account.deposit(100)
        self.assertEqual(self.my_account.balance,100)

        with self.assertRaises(ValueError):
            self.my_account.deposit(-20)


    def test_balanced(self):
        self.assertEqual(self.my_acount, 500)


    def test_withdrawed(self):
        self.my_account.withdraw(40)
        self.assertEqual(self.my_account.balance, 460)

            with self.assertRaises(ValueError):
                self.my_account.withdraw(-30)

            with self.assertRaises(ValueError):
                self.my_account.withdraw(600)






    def test_transfer_to_diferent_currency(self):
        your_account = BankAcount("Ivo",10,"&")

        with self.assertRaises(ValueError):
            self.my_account.transfer_to(your_account, 200)

        self.assertEqual(self.my_account.balance, 500)
        self.assertEqual(self.your_account.balance, 10)

    def test_transfer_to_more_money_that_we_have(self):
        your_account = BankAccount("Ivo", 10, "$")

        self.assertFalse(your_account.transfer_to(self.my_account, 300))


    def test_transfer_to(self):
        your_account = BankAccount("Ivo", 10, "$")
        result = self.my_account.transfer_to(your_account, 300)
        self.assertEqual(your_account.balance, 310)
        self.assertEqual(self.my_account.balance, 500 - 300)
        self.assertTrue(result)




if __name__ == '__main__':
    unittest.main()

