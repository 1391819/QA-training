# imports
import random


# Dice class
class Dice:
    # init
    def __init__(self, n_faces):
        self.n_faces = n_faces  # number of faces of the dice

    # roll the dice, return a random int between 1 and n of faces
    def roll(self):
        return random.randint(1, self.n_faces)
