# Try to do this both with and without elif statements.

# Asks for an input from the user as a mark.
mark = int(input("Please provide a mark: "))

"""
# If the mark is greater that 85 print "Distinction"
if mark > 85:
    print("Distinction")
# If the mark is between 65 and 85 print "Pass"
elif 65 <= mark <= 85:
    print("Pass")
# Anything else print "Fail"
else:
    print("Fail")

"""

# If the mark is greater than 65 (pass or distinction)
if mark >= 65:
    # if mark is less than 85, pass
    if mark <= 85:
        print("Pass")
    # here it can be only more than 85
    else:
        print("Distinction")
# Anything else print "Fail"
else:
    print("Fail")
