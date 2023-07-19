# imports
import dice

# main
if __name__ == "__main__":
    # throw
    dice1 = dice.throw()
    dice2 = dice.throw()

    # printing returned values
    print(f"Dice 1 rolled {dice1}")
    print(f"Dice 2 rolled {dice2}")

    # bit extra, who won?
    if dice1 > dice2:
        print(f"Dice 1 won!")
    elif dice1 < dice2:
        print(f"Dice 2 won!")
    else:
        print(f"It's a draw!")
