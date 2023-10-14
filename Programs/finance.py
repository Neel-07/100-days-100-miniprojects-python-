class PersonalFinanceTracker:
    def __init__(self):
        self.income = 0
        self.expenses = 0
        self.savings = 0
    
    def record_income(self, amount):
        # Record income
        self.income += amount
    
    def record_expense(self, amount):
        # Record an expense
        self.expenses += amount
    
    def calculate_savings(self):
        # Calculate savings
        self.savings = self.income - self.expenses

    def get_summary(self):
        # Get a summary of your financial status
        return f"Total Income: ${self.income}\nTotal Expenses: ${self.expenses}\nSavings: ${self.savings}"

# Main function
if __name__ == "__main__":
    tracker = PersonalFinanceTracker()
    
    while True:
        print("\nPersonal Finance Tracker")
        print("1. Record Income")
        print("2. Record Expense")
        print("3. Get Financial Summary")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            amount = float(input("Enter the income amount: $"))
            tracker.record_income(amount)
        elif choice == "2":
            amount = float(input("Enter the expense amount: $"))
            tracker.record_expense(amount)
        elif choice == "3":
            tracker.calculate_savings()
            print("\nFinancial Summary:")
            print(tracker.get_summary())
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please select a valid option.")
