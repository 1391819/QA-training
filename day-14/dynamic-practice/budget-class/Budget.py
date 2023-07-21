# Budget class
class Budget:
    def __init__(self, category, fund=0):
        self.category = category  # category name
        self.fund = fund  # category fund

    # withdraw specific amount from fund
    def withdraw(self, amount):
        # checking if it's possible to withdraw funds
        if self.fund < amount:
            print(f"Not enough funds")
            return False
        else:
            self.fund -= amount
            # printing new status
            print(f"Withdrawn {amount} from {self.category}")
            print(f"New fund is {self.fund}")
            return True

    # deposit specific amount to fund
    def deposit(self, amount):
        self.fund += amount
        # printing new status
        print(f"Deposited {amount} in {self.category}")
        print(f"New fund is {self.fund}")

    # transferring funds from one category to another one
    # other_category is a different Budget instance
    def transfer(self, amount, other_category):
        self.withdraw(amount)  # no code duplication
        other_category.deposit(amount)
        # printing new status
        print(
            f"{amount} was withdrawn from {self.category} to {other_category.category}"
        )
        print(f"{self.category} fund is {self.fund}")
        print(f"{other_category.category} fund is {other_category.fund}")
