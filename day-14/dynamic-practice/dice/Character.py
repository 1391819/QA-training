class Character:
    def __init__(self, name, class_, abilities):
        self.name = name
        self.class_ = class_
        self.abilities = abilities

    def show_character(self):
        print("Character:")
        print(f"Name: {self.name}")
        print(f"Class: {self.class_}")
        print("Abilities:")
        for ability, score in self.abilities.items():
            print(f"  {ability}: {score}")
