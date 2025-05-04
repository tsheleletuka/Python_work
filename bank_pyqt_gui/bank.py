class BankAccount:
    def __init__(self, owner, account_number, balance=0.0):
        self.owner = owner
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited R{amount}. New balance: R{self.balance}"
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew R{amount}. New balance: R{self.balance}"
        else:
            return "Insufficient balance or invalid amount."

    def display_balance(self):
        return f"{self.owner}'s Account ({self.account_number}): Balance = R{self.balance}"

    def transfer(self, target_account, amount):
        if 0 < amount <= self.balance:
            self.withdraw(amount)
            target_account.deposit(amount)
            return f"Transferred R{amount} to {target_account.owner}'s account."
        else:
            return "Transfer failed. Check the amount and balance."