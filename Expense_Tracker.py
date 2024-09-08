from datetime import datetime

# In-memory data storage
expenses = []

def add_expense(date, amount, category, description):
    """Add a new expense entry to the in-memory list."""
    expenses.append({
        'date': date,
        'amount': amount,
        'category': category,
        'description': description
    })

def view_expenses():
    """Display all expenses from the in-memory list."""
    print("\nAll Expenses:")
    for expense in expenses:
        print(f"Date: {expense['date']}, Amount: ${expense['amount']:.2f}, Category: {expense['category']}, Description: {expense['description']}")

def analyze_expenses():
    """Provide summary of expenses."""
    category_totals = {}
    monthly_totals = {}

    for expense in expenses:
        date = expense['date']
        amount = expense['amount']
        category = expense['category']
        month = datetime.strptime(date, '%Y-%m-%d').strftime('%Y-%m')
        
        category_totals[category] = category_totals.get(category, 0) + amount
        monthly_totals[month] = monthly_totals.get(month, 0) + amount

    print("\nCategory-wise Expenditure:")
    for category, total in category_totals.items():
        print(f"{category}: ${total:.2f}")

    print("\nMonthly Expenditure:")
    for month, total in monthly_totals.items():
        print(f"{month}: ${total:.2f}")

def main():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Analyze Expenses")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            description = input("Enter description: ")
            add_expense(date, amount, category, description)
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            analyze_expenses()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
