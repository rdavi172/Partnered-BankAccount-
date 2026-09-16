import RyanBankAccount

Reagan = RyanBankAccount.BankAccount("Reagan", 10000, 10, 6042023)

#Testing BankAccount Class
print("Reagan Account Base Information ")
Reagan.printCustomerInformation()

print("\nReagan Account deposit of $5000 ")
Reagan.deposit(5000)
Reagan.printCustomerInformation()

print("\nReagan Account withdraw of $10000 ")
Reagan.withdraw(10000)
Reagan.printCustomerInformation()

print("\nReagan Account withdraw of $10000- Beyond the amount in account ")
Reagan.withdraw(10000)

print("\nReagan Account withdraw of $5000 - Setting Account to 0 ")
Reagan.withdraw(5000)

print("\n-----End of BankAccount test-----")


#Testing SavingsAccount class

Chris = RyanBankAccount.SavingsAccount("Chris", 1000, 60, 10192005)
print("\nChris Account Base Information ")
Chris.printCustomerInformation()
print("\nChris Account gains Interest by 0.4% ")
Chris.interestAdded()
Chris.printCustomerInformation()

print("\nChris Account gains Interest by another 0.4% ")
Chris.interestAdded()
Chris.printCustomerInformation()

print("\n-----End of SavingAccount test-----")







