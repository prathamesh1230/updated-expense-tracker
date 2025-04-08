import os

def save_expense(expense):
    with open("expenses.csv", "a") as file:
        file.write(expense.to_csv())

def load_expenses():
    expenses = []
    if os.path.exists("expenses.csv"):
        with open("expenses.csv", "r") as file:
            lines = file.readlines()
            for line in lines:
                name, amount, category = line.strip().split(",")
                expenses.append((name, float(amount), category))
    return expenses

def overwrite_expenses(expenses):
    with open("expenses.csv", "w") as file:
        for e in expenses:
            file.write(f"{e[0]},{e[1]},{e[2]}\n")
