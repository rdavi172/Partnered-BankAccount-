# Author: Adrian Jaimes
# Module: checking_account.py

from bank_account import BankAccount

# 1.2: Checking account with transfer limitation
class CheckingAccount(BankAccount):
    def __init__(self, customer_name: str, current_balance: float, minimum_balance: float, account_number: str, routing_number: str, transfer_limit: float):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)
        self.transfer_limit = transfer_limit

    # idea for transfer limit enforcement
    def transfer(self, amount: float, recipient: BankAccount):
        if amount > self.transfer_limit:
            print(f"Transfer failed: ${amount:.2f} exceeds per-transaction limit of ${self.transfer_limit:.2f}.")
        elif self.current_balance - amount < self.minimum_balance:
            print("Transfer failed: Insufficient funds maintaining minimum balance.")
        else:
            self.current_balance -= amount
            recipient.current_balance += amount
            print(f"Transferred ${amount:.2f} to {recipient.customer_name}. Remaining balance: ${self.current_balance:.2f}")