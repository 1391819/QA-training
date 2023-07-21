# imports
import random


# Hat class
class Hat:
    # init
    # **balls -> collects all keyword arguments and packs them into a dict
    #            keys = colour names and values = number of balls
    def __init__(self, **balls):
        self.all_balls = []
        # for all balls (dict), save them
        for colour, amount in balls.items():
            # self.all_balls.append([colour] * amount)
            self.all_balls.extend([colour] * amount)

    # pick a random amount of balls from the hat
    def pick_balls(self):
        # number of balls to draw
        n_balls_to_draw = random.randint(1, len(self.all_balls))
        # drawn balls
        drawn_balls = random.sample(self.all_balls, n_balls_to_draw)

        # remove the drawn balls from the original balls list
        for ball in drawn_balls:
            self.all_balls.remove(ball)

        return drawn_balls

    # TODO Add probability
    def compute_probability(self):
        pass
