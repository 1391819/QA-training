import random


class Hat:
    # variable number of args
    def __init__(self, balls):
        self.all_balls = []
        for colour, amount in balls.items():
            # self.all_balls.append([colour] * amount)
            self.all_balls.extend([colour] * amount)

    def pick_balls(self):
        n_balls_to_draw = random.randint(1, len(self.all_balls))
        drawn_balls = random.sample(self.all_balls, n_balls_to_draw)

        # we need to remove the drawn balls from the original balls list
        for ball in drawn_balls:
            self.all_balls.remove(ball)

        return drawn_balls

    # TODO Add probability
    def compute_probability(self):
        pass
