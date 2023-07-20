from Hat import Hat

if __name__ == "__main__":
    # add different balls
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
