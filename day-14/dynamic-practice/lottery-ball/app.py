"""

Goal:

Create a lottery ball, or Hat, that takes a variable number of arguments that specify the number of balls of each color that are in the hat. 

Give the object the ability to pick a random number of balls from the hat, which will then be used to compute the probability of picking a certain distribution of balls over a large number of experiments

"""

# imports
from Hat import Hat

# main
if __name__ == "__main__":
    # creating Hat instance and adding different balls
    # no need to give a dict, we make use of Python's keyword args
    hat = Hat(red=20, yellow=5, black=7, pink=10, brown=3, white=1, purple=9)

    # pick a random number of balls
    drawn_balls = hat.pick_balls()

    # print picked balls
    print(f"Drawn balls: {drawn_balls}")
