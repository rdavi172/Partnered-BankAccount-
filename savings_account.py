# Author: Adrian Jaimes
# Module: savings_account.py

from bank_account import BankAccount

# 1.1: Savings account subclass with interest
class SavingsAccount(BankAccount):
    def __init__(self, customer_name: str, current_balance: float, minimum_balance: float, account_number: str, routing_number: str, interest_rate: float):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)
        self.interest_rate = interest_rate  # Annual interest rate

    # apply interest to current balance
    def apply_interest(self):
        interest = self.current_balance * self.interest_rate
        self.current_balance += interest
        print(f"Applied ${interest:.2f} interest. New balance: ${self.current_balance:.2f}")