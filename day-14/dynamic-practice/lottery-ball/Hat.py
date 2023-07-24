# imports
import random


# Hat class
class Hat:
    # init
    # balls -> collects all keyword arguments and packs them into a dict
    #          keys = colour names and values = number of balls
    def __init__(self, **balls):
        self.colours = list(balls.keys())
        self.count = list(balls.values())
        self.total_balls = sum(self.count)
        self.balls = self.unpack()  # unpacking balls dict to a list

    # unpack balls dict to a list
    def unpack(self):
        unpacked_balls = []

        # for all balls (dict), save them
        for colour, count in zip(self.colours, self.count):
            # self.all_balls.append([colour] * amount)
            unpacked_balls.extend([colour] * count)

        return unpacked_balls

    # pick a random amount of balls from the hat
    def pick_balls(self):
        # number of balls to draw
        n_balls_to_draw = random.randint(1, self.total_balls)
        # balls that were drawn
        drawn_balls = random.sample(self.balls, n_balls_to_draw)

        # removing drawn balls from hat
        for ball in drawn_balls:
            self.balls.remove(ball)

        # updating ball count
        self.total_balls -= n_balls_to_draw

        return drawn_balls

    # compute probability of picking a particular
    # distribution of balls over a certain amount of experiments
    def compute_probability(self, num_experiments, distribution):
        # amount of times the desired distribution was found
        success_count = 0

        # check to prevent computations if colour not present in hat
        if not all(color in self.colours for color in distribution.keys()):
            raise ValueError("The distribution must specify valid colours in the hat")

        for _ in range(num_experiments):
            # have a temporary hat to perform experiments
            hat_copy = self.balls.copy()
            # list of drawn balls
            drawn_balls = self.pick_balls()
            # check count for each colour - make dict of drawn distribution
            drawn_balls_counts = {
                color: drawn_balls.count(color) for color in self.colours
            }
            # if picked distribution is the one we want, update success count
            if drawn_balls_counts == distribution:
                success_count += 1
                # print("I'm here")  # debug

            # updating
            self.balls = hat_copy
            self.total_balls = len(self.balls)

        return success_count / num_experiments
