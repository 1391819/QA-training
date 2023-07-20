"""

Opens a new text file called "teams.txt" and adds the names of 5 sports teams.
Reads and displays the names of the 1st and 4th team in the file.

"""

# create new file and write to it
teams = [
    "Los Angeles Lakers",
    "Chicago Bears",
    "Dallas Cowboys",
    "New York Yankees",
    "Golden State Warriors",
]

with open("teams.txt", mode="x") as file:
    file.writelines(team + "\n" for team in teams)

# open the file and read 1st and 4th line
with open("teams.txt", mode="r") as file:
    lines = file.readlines()
    first_team = lines[0].strip()
    fourth_team = lines[3].strip()
    print(f"First team is {first_team}")
    print(f"Fourth team is {fourth_team}")
