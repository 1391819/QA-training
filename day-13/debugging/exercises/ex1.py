# funds
user_funds = 9.98

price = {"Burger": 9.99, "Pizza": 4.99, "Hot Dog": 2.99}

item_price = price["Burger"]

if item_price < user_funds:
    print("You have enough money!")
if item_price == user_funds:
    print("You have the precise amount of money")
if item_price > user_funds:
    print("Sorry you don't have enough money.")
