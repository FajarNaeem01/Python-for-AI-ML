"""
===============================================
Python for AI/ML Engineering
Phase 0 - Professional Python

Day 05 - OOP Fundamentals
Practice File

Author: Fajar Naeem Rana
===============================================
"""
class BankAccount:
    bank_name = "HBL "
    def __init__(self,account_holder, account_number, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def display_account(self):
        print("\n=========== Account Summary ============")
        print(f"Bank Name: {BankAccount.bank_name}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: {self.balance}")
        print(f"Account Active: {self.is_active()}")
        print("=========================================")

    def deposit(self, amount):
        self.balance += amount
        return amount

    def withdraw(self,amount):
        if amount > self.balance:
            
            return False
        else:
            self.balance -= amount
            return True

    def current_balance(self):
        return self.balance

    def is_active(self):
        if self.balance >= 0:
            return True
        else:
            return False

    def transfer(self, other_account, amount):
        self.balance -= amount
        other_account.deposit(amount)
        return amount

account1 = BankAccount("Fajar", "PK001", 5000)
account2 = BankAccount("Noor", "PK002", 10000)

account1.display_account()
account2.display_account()

amount= account1.deposit(4000)
print(f"\n{amount} Deposited!")
print(f"Current Balance: {account1.current_balance()}")

amount= account1.transfer(account2, 3000)
print(f"{amount} transferred to {account2.account_holder}")

if account1.withdraw(1500):
    print("\nRs 1500 Withdrawn!")
    print(f"Current Balance: {account1.current_balance()}")
else:
    print("\nLow Balance! Cannot withdraw money.")

if account1.withdraw(10000):
    print("\nRs 10,000 Withdrawn!")
    print(f"Current Balance: {account1.current_balance()}")
else:
    print("\nLow Balance! Cannot withdraw money.")

BankAccount.bank_name= "HBL Bank"
account1.display_account()
account2.display_account()