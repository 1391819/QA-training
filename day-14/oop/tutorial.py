from abc import ABC, abstractclassmethod


# superclass
class Bird(ABC):
    fly = True
    babies = 0
    extinct = False

    def noise(self):
        return "Squawk"

    def reproduce(self):
        self.babies += 1

    @abstractclassmethod
    def eat(self):
        pass


# subclass - Inheritance
class Owl(Bird):
    # polymorphism
    def reproduce(self):
        self.babies += 6

    # abstraction
    def eat(self):
        return "Peck peck"


# subclass - inheritance
class Dodo(Bird):
    Fly = False  # polymorphism
    extinct = True  # polymorphism

    def eat(self):
        return "Nom nom"

    # polymorphism
    def reproduce(self):
        if not self.extinct:
            # encapsulation
            # babies var not being directly
            # accesses
            self.babies += 1
