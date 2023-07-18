# https://www.w3resource.com/python-exercises/python-conditional-statements-and-loop-exercises.php

# indicating symbol
char = "*"

# print character 5 times
# from 1 just to avoid the first blank print
# -> looks better with the first blank line
for i in range(0, 5):  # range(1, 6)
    print(char * i)

# reverse range
for j in range(5, 0, -1):
    print(char * j)
