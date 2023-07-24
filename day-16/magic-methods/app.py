class Dog:
    # magic method #1
    # one of the two methods called when we instantiate a class
    def __init__(self, name: str, age: int, breed: str) -> None:
        self.name = name
        self.age = age
        self.breed = breed

        # does pretty much nothing BUT

    # --------------------------------------------------------------------------------

    # two of the two methods called when we instantiate a class
    # this is called before __init__, that's why we can instantiate
    # an object even without an __init__ method
    # def __new__():

    # --------------------------------------------------------------------------------

    # magic method #2
    # particularly useful to have defined
    # called when we print out the object (instead of memory allocation)
    # although sometimes, for debugging purposes, seeing the memory allocation is good
    def __str__(self):
        return f"A {self.age} year old {self.breed} called {self.name}"

    # --------------------------------------------------------------------------------

    # magic method #3
    # conversion can also be done to float
    def __int__(self):
        return self.age

    # --------------------------------------------------------------------------------

    # magic method #4
    # under which circumstances the object is True or False
    def __bool__(self):
        # here, if breed is not an empty string, meaning is True
        return self.breed != ""

    # --------------------------------------------------------------------------------

    # magic method #5
    # overriding operations (+, -, etc)
    def __add__(self, other_dog):
        return Dog(
            self.name + other_dog.name,
            self.age + other_dog.age,
            self.breed + other_dog.breed,
        )


if __name__ == "__main__":
    # fido = Dog()  # Dog.__new__() gets called

    # --------------------------------------------------------------------------------

    # Dog.__new__() gets called, then it goes into Dog.__init__(attributes)
    fido2 = Dog("fido", 5, "labrador")

    # --------------------------------------------------------------------------------

    print(fido2)
    print(str(fido2).upper())  # can also use methods on conversion method
    print(fido2.__str__())  # can also be called directly, but useless pretty much

    # --------------------------------------------------------------------------------

    print(int(fido2))  # override done, age is printed

    # --------------------------------------------------------------------------------

    print(bool(fido2))  # override done, if breed is set it's True
    if fido2:
        print("Fido is True")
    else:
        print("Fido is False")

    # --------------------------------------------------------------------------------

    black = Dog("Black", 7, "Husky")

    puppy = fido2 + black  # + has been overwritten
    print(puppy)  # uses overwritten +
