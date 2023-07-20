class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.avg_test_score = 0
        self.score1 = 0
        self.score2 = 0
        self.score3 = 0

    def get_avg_test_score(self):
        self.avg_test_score = (self.score1 + self.score2 + self.score3) / 3
        return self.avg_test_score


# John = Student("John", "21")
# Jane = Student("Jane", "22")

# print(getattr(John, "age"))
# print(John.age)
