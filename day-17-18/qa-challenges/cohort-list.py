"""

Write a program which will do the following:
- Create a list which contains the first name of everyone in your cohort and store it in a variable called team.
- Add your trainer to the list without manually editing it.
- Print the list to the terminal.
- Print only the 5th person in the list to your terminal.
- Print the number of times Chris occurs in the list team, to the terminal.

"""


if __name__ == "__main__":
    team = ["Roberto", "Chris", "Andrei", "Akber", "Athena", "Chris"]

    team.append("Adam")

    print(team)

    print(team[4])

    print(team.count("Chris"))
