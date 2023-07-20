import random


class Dice:
    def __init__(self, n_faces):
        self.n_faces = n_faces

    def roll(self):
        return random.randint(1, self.n_faces)
