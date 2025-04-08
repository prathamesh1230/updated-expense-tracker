from storage import save_expense, load_expenses, overwrite_expenses
from models import Expense

def add_expense(name, amount, category):
    expense = Expense(name, amount, category)
    save_expense(expense)

def view_expenses():
    expenses = load_expenses()
    if not expenses:
        print("📂 No expenses found.")
    else:
        print("\n📋 Expense List:")
        for idx, (name, amount, category) in enumerate(expenses, start=1):
            print(f"{idx}. {name} - ₹{amount} [{category}]")

def delete_expense(index):
    expenses = load_expenses()
    if 0 < index <= len(expenses):
        removed = expenses.pop(index - 1)
        overwrite_expenses(expenses)
        print(f"✅ Deleted: {removed[0]} - ₹{removed[1]}")
    else:
        print("❌ Invalid index.")

def total_expense():
    expenses = load_expenses()
    total = sum(amount for _, amount, _ in expenses)
    print(f"\n💰 Total Expense: ₹{total}")
