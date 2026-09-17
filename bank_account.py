# Author: Adrian Jaimes
# Module: bank_account.py

class BankAccount:
    bank_title = "SECU Bank"

    def __init__(self, customer_name: str, current_balance: float, minimum_balance: float, account_number: str,
                 routing_number: str):
        # Public instance attributes
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance

        #  2.1: Protected member
        self._account_number = account_number

        #  2.2: Private member
        self.__routing_number = routing_number


    def get_routing_number(self):
        return self.__routing_number


    def deposit(self, amount: float):
        if amount > 0:
            self.current_balance += amount
            print(f"Deposited ${amount:.2f}. New balance:${self.current_balance:.2f}")
        else:
            print("Deposit amount must be positive.")


    def withdraw(self, amount: float):
        if self.current_balance - amount < self.minimum_balance:
            print(
                f"Withdrawal denied for {self.customer_name}. Remaining balance (${self.current_balance - amount:.2f}) would be less than minimum balance (${self.minimum_balance:.2f}).")
            return False
        else:
            self.current_balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance:${self.current_balance:.2f}")
            return True

    def print_customer_information(self):
        print(f"Bank Name: {BankAccount.bank_title}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Account Number (Protected): {self._account_number}")
        print(f"Routing Number (Private): {self.__routing_number}")
        print(f"Current Balance: ${self.current_balance:.2f}")
        print(f"Minimum Balance: ${self.minimum_balance:.2f}")
        print("-" * 30)