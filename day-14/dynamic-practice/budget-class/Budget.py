class Budget:
    def __init__(self, category, fund=0):
        self.category = category  # category name
        self.fund = fund  # category fund

    # withdraw specific amount from fund
    def withdraw(self, amount):
        # checking if it's possible to withdraw funds
        if self.fund < amount:
            print(f"Not enough funds")
        else:
            self.fund -= amount
            # printing new status
            print(f"Withdrawn {amount} from {self.category}")
            print(f"New fund is {self.fund}")

    # deposit specific amount to fund
    def deposit(self, amount):
        self.fund += amount
        # printing new status
        print(f"Deposited {amount} in {self.category}")
        print(f"New fund is {self.fund}")

    # transferring funds from one category to another one
    # other_category is a different Budget instance
    def transfer(self, amount, other_category):
        # checking if it's possible to withdraw funds
        if self.fund < amount:
            print(f"Not enough funds")
        else:
            self.fund -= amount  # withdraw from one category
            other_category.fund += amount  # deposit into the other
            # printing new status
            print(
                f"{amount} was withdrawn from {self.category} to {other_category.category}"
            )
            print(f"{self.category} fund is {self.fund}")
            print(f"{other_category.category} fund is {other_category.fund}")
