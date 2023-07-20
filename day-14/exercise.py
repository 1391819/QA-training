"""
In a new Python file, create a class of students.
It should contain the following attributes: name, age, and class with default value "student".

It should also contain a method which takes in 3 test scores and prints the students average test score.
"""

from tutorial import Student


class Class_:
    def __init__(self, class_name, student_list):
        self.class_name = class_name
        self.student_list = student_list

    def get_avg_test_score(self, score1, score2, score3):
        return (score1 + score2 + score3) / 3

    def get_all_students(self):
        for student in self.student_list:
            print(student.name)


students_list = [Student("Mary", "18"), Student("John", "19"), Student("Mark", "22")]

new_class = Class_("Comp Sci", students_list)

new_class.get_all_students()
