# imports
import random


# Hat class
class Hat:
    # balls -> collects all keyword arguments and packs them into a dict
    #          keys = colour names and values = number of balls
    def __init__(self, **balls):
        self.colours = list(balls.keys())  # all present colours in the hat
        self.count = list(balls.values())  # number of balls in the hat
        self.total_balls = sum(self.count)  # total number of balls in the hat
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

    # compute probability of picking a particular distribution of balls over a certain amount of experiments
    def compute_probability(self, num_experiments, distribution):
        # amount of times the desired distribution was found
        success_count = 0

        # check that the hat contains the distribution colours
        distribution_colours = list(distribution.keys())  # get "asked" colours
        if not all(colour in self.colours for colour in distribution_colours):
            raise ValueError("The distribution must specify valid colours in the hat")

        # have a temporary hat to perform experiments - the same object could be reused but for simplicity
        # I will do it this way
        tmp_hat_balls = self.balls.copy()
        tmp_hat_colours = self.colours.copy()  # all present colours in the tmp hat
        tmp_hat_total_balls = self.total_balls  # total number of balls in the tmp hat

        for _ in range(num_experiments):
            # number of balls to draw
            n_balls_to_draw = random.randint(1, tmp_hat_total_balls)
            # balls that were drawn
            # we do not remove them from the hat since we are just trying to compute the
            # probability
            # if we'd want to remove them from the hat, we'd have to handle possible valueerrors
            drawn_balls = random.sample(tmp_hat_balls, n_balls_to_draw)

            # check count for each colour - make dict of drawn distribution
            drawn_balls_counts = {
                colour: drawn_balls.count(colour) for colour in tmp_hat_colours
            }
            # if picked distribution is the one we want, update success count
            if drawn_balls_counts == distribution:
                success_count += 1

        return success_count / num_experiments
