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
    hat = Hat(
        {
            "Red": 20,
            "Yellow": 5,
            "Black": 7,
            "Pink": 10,
            "Brown": 3,
            "White": 1,
            "Purple": 9,
        }
    )

    # pick a random number of balls
    drawn_balls = hat.pick_balls()

    # print picked balls
    print(f"Drawn balls: {drawn_balls}")
