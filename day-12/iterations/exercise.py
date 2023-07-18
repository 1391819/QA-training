# Write a while loop which asks for the names of 5 people
# and for each person prints their name followed
# by the text "is awesome!"

# Using a for loop

"""
# loop 5 times
for i in range(5):
    name = input("Enter your name: ")
    print(f"{name} is awesome!")
"""


# Using a simple while loop

"""
people = 0
while people < 5:
    name = input("Enter your name: ")
    print(f"{name} is awesome!")
    people += 1
"""

# a bit different?

# most likely overcomplicated but just to practice more things
people_list = []
while len(people_list) < 5:
    name = input(f"Person #{len(people_list) + 1} name: ")
    people_list.append(name)

for person in people_list:
    print(f"{person} is awesome!")

# Work out what the following for loop does:
#
#   print numbers from 10 to 21, using a step of 2
#   10, 12, 14, 16, 18, 20
for i in range(10, 21, 2):
    print(i)
