import mymodule


if __name__ == "__main__":
    dice1 = mymodule.random_n_in_range(1, 6)
    dice2 = mymodule.random_n_in_range(1, 6)

    print(f"Dice 1 rolled {dice1}")
    print(f"Dice 2 rolled {dice2}")

    if dice1 > dice2:
        print(f"Dice 1 won!")
    elif dice1 < dice2:
        print(f"Dice 2 won!")
    else:
        print(f"It's a draw!")
