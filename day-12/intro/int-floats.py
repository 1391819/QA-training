number1 = input("Enter whole number: ")
number2 = input("Enter decimal number: ")

integer_number = int(number1)
float_number = float(number2)
# is the below int cast really needed?
round_number = int(round(float_number))  # old
round_number2 = round(float_number)  # new

print(number1)  # int
print(number2)  # float
print(type(round_number))  # debug
print(type(round_number2))
print(round_number)  # rounded float
print(round_number2)  # rounded float
