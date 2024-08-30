# Base class
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposite(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}"
        return "Deposit amount must be positive."

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"Withdraw ${amount:.2f}. New balance: ${self.balance:.2f}"
        elif amount > self.balance:
            return "Insufficient funds."
        return "Withdrawal amount must be positive."
    
    def display_info(self):
        return f"Account Number: {self.account_number}, Balance: ${self.balance:.2f}"

# Derived class
class SavingAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calcualte_interest(self):
        interest = self.balance * (self.interest_rate/100)
        return f"Interest earned: ${interest:.2f}"


    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Interest Rate: {self.interest_rate}%"

# derived class
class CheckingAccount(BankAccount):
    def __init__(self, account_number, balance, monthly_fees):
        super().__init__(account_number, balance)
        self.monthly_fees = monthly_fees

    def deduct_fees(self):
        if self.balance >= self.monthly_fees:
            self.balance -= self.monthly_fees
            return f"monthly fee of ${self.monthly_fees:.2f} deducted.New balance: ${self.balance:.2f}"
        return "Insufficient funds to deduct the monthly fee."

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Monthly Fee: ${self.monthly_fees:.2f}"
    
# Example usage
saving_account = SavingAccount(account_number="123456789", balance=1000, interest_rate=2.5)
checking_account = CheckingAccount(account_number="9876543231", balance=500, monthly_fees=10)
print()
print(saving_account.display_info())
print(saving_account.calcualte_interest())

print()
print(checking_account.display_info())
print(checking_account.deduct_fees())