# funds
user_funds = 9.98
# declaring dictionary
price = {"Burger": 9.99, "Pizza": 4.99, "Hot Dog": 2.99}
# retrieving item price
item_price = price["Burger"]

# fixed syntax and logical errors
if item_price < user_funds:
    print("You have enough money!")
# not assignment but check -> = to ==
if item_price == user_funds:
    print("You have the precise amount of money")
# from < to >
if item_price > user_funds:
    print("Sorry you don't have enough money.")
