class Expense:
    def __init__(self, name, amount, category):
        self.name = name
        self.amount = amount
        self.category = category

    def to_csv(self):
        return f"{self.name},{self.amount},{self.category}\n"
