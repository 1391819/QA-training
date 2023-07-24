"""

Goal:

Create a lottery ball, or Hat, that takes a variable number of arguments that specify the number of balls of each color that are in the hat. 

Give the object the ability to pick a random number of balls from the hat, which will then be used to compute the probability of picking a certain distribution of balls over a large number of experiments

"""

# imports
from Hat import Hat

if __name__ == "__main__":
    """Main"""

    # creating Hat instance and adding different balls
    # no need to give a dict, we make use of Python's keyword args
    hat = Hat(red=3, yellow=5, black=7, pink=2)

    # pick a random number of balls
    drawn_balls = hat.pick_balls()
    # print picked balls
    # print(f"Drawn balls: {drawn_balls}")

    # compute probability of picking a particular
    # distribution of balls over a certain amount of experiments
    num_experiments = 5000
    distribution = {
        "red": 2,
        "yellow": 1,
        "pink": 1,
    }
    probability = hat.compute_probability(num_experiments, distribution)
    # : -> start of string formatting (float numbers)
    # .4f ->
    #       .4 -> four decimal places
    #       f -> floating-point number
    print(f"Probability of picking {distribution} is {probability:.4f}")
