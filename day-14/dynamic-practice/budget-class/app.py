"""

Goal: “Create a Budget class that can instantiate objects based on different budget categories like food, clothing, and entertainment. These objects should allow for depositing and withdrawing funds from each category, as well computing category balances and transferring balance amounts between categories”

"""

# imports
from Budget import Budget

if __name__ == "__main__":
    # Budget class
    food = Budget("Food", 50)
    clothing = Budget("Clothing", 100)
    entertainment = Budget("Entertainment", 150)

    print(f"{food.category} fund is {food.fund}")
    print(f"{clothing.category} fund is {clothing.fund}")
    print(f"{clothing.category} fund is {clothing.fund}")
    print()

    food.withdraw(5000)
    clothing.deposit(50)
    entertainment.deposit(100)

    food.transfer(5, clothing)
