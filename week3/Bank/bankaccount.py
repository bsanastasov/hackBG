class BankAccount():
	def __init__(self, name, balance, currency):
		self.name = name
		self.balance = balance
		self.currency = currency
        self.history = ["Account was created"]

	def deposite(self, amount):

		if amount < 0:
            raise ValueError

        self.balance += amount
        self.history.append("{}{} was deposited.").format(amount, self.currency)


    def balanced(self):
        return self.balance


    def withdraw (self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.history.append("{}{} was withdrawed").format(self.amount, self.currency)
        else:
            self.histry.append("Withdraw failed!")


    def __str__(self):
        message = "Bank acccount for {} with balance of {}{}"
        return message.format(self.name, self.balance, self.currency)

    def transfer_to(self, account, amount):
        if self.currency != account.currency:
            raise ValueError

        if self.balance > amount:
            return False


        account.history.append('Transfer from {} for {}{}'.format(self.name, amount, self.currency))
        self.history.append('Transfer to {} for {}{}'.format(account.name, amount, self.currency)
        self.balance -= amount
        account.balance += amount
        return True


    def history_to(self):
        mess = "Acount was created", "Deposited {}", "Balance checked -> {}", "__int__ check -> {}", "{} was withdrawed", "Balance check -> {}"
        return mess.format(self.balance, self.balance, self.balance, )

    def history(self):
        return self.history


