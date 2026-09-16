class BankAccount:
    Title = "Bank of America"
    def __init__(self, name, currentBalance, MinimumBalance):
        self.name = name
        self.currentBalance = currentBalance
        self.minimumBalance = MinimumBalance

    def deposit(self, amount):
        self.currentBalance += amount

    def withdraw(self, amount):
        if amount > self.minimumBalance:
            print("Insufficient funds")
            return
        self.currentBalance -= amount

    def printCustomerInformation(self):
        print(f'Bank Title: {self.Title} \nCustomer Name: {self.name} '
              f'\nBalance: {self.currentBalance} \nMinimum Balance: {self.minimumBalance}')

person1 = BankAccount("Reagan", 10000, 50)
person2 = BankAccount("Jill", 100, 100)

person1.deposit(5000)
person1.printCustomerInformation()
person2.withdraw(50)
person2.printCustomerInformation()
person2.withdraw(500)
person2.printCustomerInformation()