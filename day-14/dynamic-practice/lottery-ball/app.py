"""

Goal:

Create a lottery ball, or Hat, that takes a variable number of arguments that specify the number of balls of each color that are in the hat. 

Give the object the ability to pick a random number of balls from the hat, which will then be used to compute the probability of picking a certain distribution of balls over a large number of experiments

"""

# imports
from Hat import Hat

if __name__ == "__main__":
    # creating Hat instance and adding different balls
    hat = Hat(red=50, yellow=50)

    # pick a random number of balls
    drawn_balls = hat.pick_balls()
    # print picked balls
    print(f"Drawn balls: {drawn_balls}")

    # compute probability of picking a particular
    # distribution of balls over a certain amount of experiments
    num_experiments = 500
    distribution = {
        "red": 25,
        "yellow": 25,
    }
    probability = hat.compute_probability(num_experiments, distribution)
    # : -> start of string formatting (float numbers)
    # .4f ->
    #       .4 -> four decimal places
    #       f -> floating-point number
    print(f"Probability of picking {distribution} is {probability:.4f}")
