# https://www.w3resource.com/python-exercises/python-conditional-statements-and-loop-exercises.php


# converting temp to fahrenheit
def convert_to_fahrenheit(temp):
    temp = int(temp)  # casting to int
    temp = (temp * 9 / 5) + 32  # converting to fahrenheit

    return round(temp)  # rounding, not needed but looks better?


# converting temp to celsius
def convert_to_celsius(temp):
    temp = int(temp)  # casting to int
    temp = (5 / 9) * (temp - 32)  # converting to celsius

    return round(temp)  # rounding, not needed but looks better?


# let user decide whether he's going to enter °C or °F
pick = input("°C or °F? ")

if pick == "C":
    # user input
    celsius = input("Enter temperature in °C: ")
    # convert
    fahrenheit = convert_to_fahrenheit(celsius)
    # print
    print(f"The converted temperature is {fahrenheit}°F")
elif pick == "F":
    # user input
    fahrenheit = input("Enter temperature in °F: ")
    # convert
    celsius = convert_to_celsius(fahrenheit)
    # print
    print(f"The converted temperature is {celsius}°C")
else:
    # this could be remade into a while loop
    # until user enters valid entry
    print("You selected an invalid entry")
