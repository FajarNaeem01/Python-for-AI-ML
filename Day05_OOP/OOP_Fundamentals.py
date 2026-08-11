"""
===============================================
Python for AI/ML Engineering
Phase 0 - Professional Python

Day 05 - OOP Fundamentals
Practice File

Author: Fajar Naeem Rana
===============================================
"""
#==============================================
#            BankAccount Class 
#==============================================
class BankAccount:
    bank_name = "HBL "
    def __init__(self,account_holder, account_number, balance):
        self.account_holder = account_holder   # attribute initilization
        self.account_number = account_number
        self.__balance = balance               # private access

    def display_account(self):
        print("\n=========== Account Summary ============")
        print(f"Bank Name: {BankAccount.bank_name}")   # accessing class attribute
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: {self.__balance}")
        print(f"Account Active: {self.is_active()}")   # calling other method
        print("=========================================")

    def deposit(self, amount):
        if amount <=0:
            print("Invalid! Deposit Rejected")
        self.__balance += amount     # changing object's state
        return amount

    def withdraw(self,amount):

        if amount > self.__balance or amount < 0:
            return False, amount
        else:
            self.__balance -= amount
            return True, amount  # returning multiple variables

    def current_balance(self):
        return self.__balance

    def is_active(self):
        if self.__balance >= 0:
            return True
        else:
            return False

    def transfer(self, other_account, amount):
        if amount > self.__balance or amount <= 0:
            print("Invalid! Transfer Rejected.")
        self.__balance -= amount
        other_account.deposit(amount)
        return amount

# =============================================
# ============= Creating objects ==============
account1 = BankAccount("Fajar", "PK001", 5000)
account2 = BankAccount("Noor", "PK002", 10000)

print("Accounts detail before any operation:")
account1.display_account()
account2.display_account()

# ============== Deposit ===============
amount= account1.deposit(4000)
print(f"\n{amount} Deposited!")
print(f"Current Balance: {account1.current_balance()}")

# ============= Transfer ================
amount= account1.transfer(account2, 3000)
print(f"{amount} transferred to {account2.account_holder}")

# ============= withdrawal ===============
amount = float(input("Enter amount to withdraw: "))
is_withdrawn, amount_withdrawn = account1.withdraw(amount)
if is_withdrawn:
    print(f"{amount_withdrawn} is withdrawn")
else:
    print("Invalid! Withdrawal Rejected")

# ====== changing class atrribute ========
BankAccount.bank_name= "HBL Bank"
account1.display_account()
account2.display_account()