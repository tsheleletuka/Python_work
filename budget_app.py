import json

# Define the data structure for storing transactions
class Transaction:
    def __init__(self, t_type, amount, category, description):
        self.t_type = t_type  # 'income' or 'expense'
        self.amount = amount
        self.category = category
        self.description = description

    def to_dict(self):
        return {
            "type": self.t_type,
            "amount": self.amount,
            "category": self.category,
            "description": self.description
        }

# Load data from a file
def load_data():
    try:
        with open("finance_data.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []
    return data

# Save data to a file
def save_data(data):
    with open("finance_data.json", "w") as f:
        json.dump(data, f, indent=4)

# Add a transaction
def add_transaction(data, t_type, amount, category, description):
    transaction = Transaction(t_type, amount, category, description)
    data.append(transaction.to_dict())
    save_data(data)
    print(f"Added {t_type} of R{amount} in category '{category}'.")

# View summary
def view_summary(data):
    total_income = sum(item["amount"] for item in data if item["type"] == "income")
    total_expenses = sum(item["amount"] for item in data if item["type"] == "expense")
    balance = total_income - total_expenses
    print(f"Total Income: R{total_income}")
    print(f"Total Expenses: R{total_expenses}")
    print(f"Balance: R{balance}")

# View expenses by category
def view_by_category(data):
    categories = {}
    for item in data:
        category = item["category"]
        if category in categories:
            categories[category] += item["amount"]
        else:
            categories[category] = item["amount"]
    
    for category, total in categories.items():
        print(f"{category}: R{total}")

# Main app interface
def main():
    data = load_data()
    
    while True:
        print("\n--- Personal Finance Tracker ---")
        print("1. Add Transaction")
        print("2. View Summary")
        print("3. View Expenses by Category")
        print("4. Exit")
        
        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            t_type = input("Enter transaction type (income/expense): ").strip().lower()
            amount = float(input("Enter amount: "))
            category = input("Enter category: ").strip()
            description = input("Enter description: ").strip()
            add_transaction(data, t_type, amount, category, description)
        
        elif choice == "2":
            view_summary(data)
        
        elif choice == "3":
            view_by_category(data)
        
        elif choice == "4":
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
