"""
Goal: “Create a Budget class that can instantiate objects based on different budget categories like food, clothing, and entertainment. These objects should allow for depositing and withdrawing funds from each category, as well computing category balances and transferring balance amounts between categories”
"""


class Budget:
    def __init__(self, category, fund=0):
        self.category = category
        self.fund = fund

    def withdraw(self, amount):
        if self.fund < amount:
            print(f"Not enough funds")
        else:
            self.fund -= amount
            print(f"Withdrawn {amount} from {self.category}")
            print(f"New fund is {self.fund}")

    def deposit(self, amount):
        self.fund += amount
        print(f"Deposited {amount} in {self.category}")
        print(f"New fund is {self.fund}")

    def transfer(self, amount, other_category):
        if self.fund < amount:
            print(f"Not enough funds")
        else:
            self.fund -= amount
            other_category.fund += amount
            print(
                f"{amount} was withdrawn from {self.category} to {other_category.category}"
            )
            print(f"{self.category} fund is {self.fund}")
            print(f"{other_category.category} fund is {other_category.fund}")
