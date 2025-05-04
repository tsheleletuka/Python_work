import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QPushButton, QMessageBox,
                             QInputDialog)
from bank import BankAccount

accounts = {}

class BankApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bank Account PyQt App")
        self.setGeometry(100, 100, 300, 300)

        layout = QVBoxLayout()

        actions = [
            ("Create Account", self.create_account),
            ("Deposit", self.deposit),
            ("Withdraw", self.withdraw),
            ("Check Balance", self.check_balance),
            ("Transfer", self.transfer),
            ("Exit", self.close)
        ]

        for text, method in actions:
            button = QPushButton(text)
            button.clicked.connect(method)
            layout.addWidget(button)

        self.setLayout(layout)

    def get_text(self, prompt):
        text, ok = QInputDialog.getText(self, "Input", prompt)
        return text if ok else None

    def get_float(self, prompt):
        value, ok = QInputDialog.getDouble(self, "Input", prompt)
        return value if ok else None

    def show_message(self, message):
        QMessageBox.information(self, "Info", message)

    def create_account(self):
        owner = self.get_text("Enter account holder's name:")
        acc_number = self.get_text("Enter account number:")
        if not owner or not acc_number:
            return
        if acc_number in accounts:
            self.show_message("Account already exists.")
            return
        balance = self.get_float("Enter initial balance:")
        if balance is None:
            return
        accounts[acc_number] = BankAccount(owner, acc_number, balance)
        self.show_message("Account created successfully.")

    def deposit(self):
        acc_number = self.get_text("Enter account number:")
        if acc_number not in accounts:
            self.show_message("Account not found.")
            return
        amount = self.get_float("Enter amount to deposit:")
        if amount is None:
            return
        result = accounts[acc_number].deposit(amount)
        self.show_message(result)

    def withdraw(self):
        acc_number = self.get_text("Enter account number:")
        if acc_number not in accounts:
            self.show_message("Account not found.")
            return
        amount = self.get_float("Enter amount to withdraw:")
        if amount is None:
            return
        result = accounts[acc_number].withdraw(amount)
        self.show_message(result)

    def check_balance(self):
        acc_number = self.get_text("Enter account number:")
        if acc_number not in accounts:
            self.show_message("Account not found.")
            return
        result = accounts[acc_number].display_balance()
        self.show_message(result)

    def transfer(self):
        from_acc = self.get_text("From account number:")
        to_acc = self.get_text("To account number:")
        if from_acc not in accounts or to_acc not in accounts:
            self.show_message("One or both accounts not found.")
            return
        amount = self.get_float("Amount to transfer:")
        if amount is None:
            return
        result = accounts[from_acc].transfer(accounts[to_acc], amount)
        self.show_message(result)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BankApp()
    window.show()
    sys.exit(app.exec_())