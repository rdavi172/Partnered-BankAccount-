# Author: Adrian Jaimes
# Module: main.py

#  3.1/3.2: Separate main file importing SavingsAccount and CheckingAccount
from savings_account import SavingsAccount
from checking_account import CheckingAccount


def main():
    print("=== BANKING SYSTEM DEMO ===\n")

    #  4: two SavingsAccount instances
    savings1 = SavingsAccount("Alice Smith", 1000.0, 100.0, "SAV-1001", "RT-987654", interest_rate=0.03)
    savings2 = SavingsAccount("Bob Jones", 500.0, 50.0, "SAV-1002", "RT-987654", interest_rate=0.05)

    # 4: two CheckingAccount instances
    checking1 = CheckingAccount("Charlie Brown", 800.0, 50.0, "CHK-2001", "RT-987654", transfer_limit=200.0)
    checking2 = CheckingAccount("Diana Prince", 1500.0, 100.0, "CHK-2002", "RT-987654", transfer_limit=500.0)

    #  3.3: Illustrate scenario using methods

    # Scenario 1: Savings interest application and account display
    print("--- Savings Account Operations ---")
    savings1.print_customer_information()
    savings1.deposit(200.0)
    savings1.apply_interest()  # Applies 3% interest
    print()

    savings2.print_customer_information()
    savings2.apply_interest()  # Applies 5% interest
    print()

    # Scenario 2: Checking transfer limit testing
    print("--- Checking Account Transfer Operations ---")
    checking1.print_customer_information()

    # sttempt transfer exceeding limit
    checking1.transfer(250.0, checking2)

    # successful transfer within limit
    checking1.transfer(150.0, checking2)
    print()

    checking2.print_customer_information()


if __name__ == "__main__":
    main()