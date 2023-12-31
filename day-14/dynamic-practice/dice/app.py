"""

- Write a class called Dice
- When initialised the object will set how many faces the die has
- Create objects for 6, 20, 2 and 4 sided die.
- Roll a charactor sheet for a Swashbuckler Rogue called 'Earl Grey' DnD 5th ed.

"""

# imports
from Dice import Dice
from Character import Character

# main
if __name__ == "__main__":
    # creating Dice instances, different amount of faces
    dice_6 = Dice(6)
    dice_20 = Dice(20)
    dice_2 = Dice(2)
    dice_4 = Dice(4)

    # rolling each dice
    print(f"6-sided roll: {dice_6.roll()}")
    print(f"20-sided roll: {dice_20.roll()}")
    print(f"2-sided roll: {dice_2.roll()}")
    print(f"4-sided roll: {dice_4.roll()}")
    print()

    # rolling DnD character
    name = "Earl Grey"
    class_ = "Swashbuckler Rogue"
    abilities = {
        "Strength": dice_20.roll(),
        "Dexterity": dice_20.roll(),
        "Constitution": dice_20.roll(),
        "Intelligence": dice_20.roll(),
        "Wisdom": dice_20.roll(),
        "Charisma": dice_20.roll(),
    }

    # creating instance of Character
    new_char = Character(name, class_, abilities)
    # displaying stats
    new_char.show_character()
