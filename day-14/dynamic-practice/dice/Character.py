# Character class
class Character:
    # init
    def __init__(self, name, class_, abilities):
        self.name = name  # name
        self.class_ = class_  # class (using trail _ to avoid keyword conflicts)
        self.abilities = abilities  # character abilities

    # printing stats of the character
    def show_character(self):
        print("Character:")
        print(f"Name: {self.name}")
        print(f"Class: {self.class_}")
        print("Abilities:")
        # for each ability, print its score
        for ability, score in self.abilities.items():
            print(f"  {ability}: {score}")
