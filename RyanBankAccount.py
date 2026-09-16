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

class SavingsAccount (BankAccount):
    def interestAdded(self):
        self.currentBalance += self.currentBalance*0.004

class CheckingAccount (BankAccount):
    def Transfer(self, amount):
        if amount > 100:
            print("Transfer exceeds limit of 100")
        elif amount > self.currentBalance:
            print("Insufficient funds")
        elif amount < 0:
            print("Unable to transfer $0 or less")
        else:
            self.currentBalance -= amount
            print(f'Transfer of Amount: {amount} successful')
