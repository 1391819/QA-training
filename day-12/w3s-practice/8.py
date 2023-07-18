# https://www.w3resource.com/python-exercises/python-conditional-statements-and-loop-exercises.php

# 0 to 5, 6 already excluded
for i in range(6):
    # we do not print number 3
    if i == 3:
        continue
    print(i)
