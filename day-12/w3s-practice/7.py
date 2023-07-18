# https://www.w3resource.com/python-exercises/python-conditional-statements-and-loop-exercises.php

# list declaration
datalist = [
    1452,
    11.23,
    1 + 2j,
    True,
    "w3resource",
    (0, -1),
    [5, 12],
    {"class": "V", "section": "A"},
]

# for each item in the list
for item in datalist:
    # print item and its type
    print(f"{item} is a {type(item)}")
