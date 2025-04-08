from tracker import add_expense, view_expenses, delete_expense, total_expense
from utils import get_float_input

def main():
    while True:
        print("\n💸 Expense Tracker Menu")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. View Total Expense")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter expense name: ")
            amount = get_float_input("Enter amount (₹): ")
            category = input("Enter category: ")
            add_expense(name, amount, category)
            print("✅ Expense added.")
        
        elif choice == "2":
            view_expenses()
        
        elif choice == "3":
            view_expenses()
            index = int(input("Enter index to delete: "))
            delete_expense(index)
        
        elif choice == "4":
            total_expense()
        
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
