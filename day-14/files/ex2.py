"""

Edits your "teams.txt" file so that the top line is replaced with "This is a new line".
Print out the edited file line by line.

"""

# first, we get all the content of teams.txt file
current_data = []

with open("teams.txt", mode="r") as file:
    current_data = file.readlines()

# now, we add the new line at the start of the list
new_line = "This is a new line\n"
current_data.insert(0, new_line)

with open("teams.txt", mode="w") as file:
    file.writelines(current_data)
