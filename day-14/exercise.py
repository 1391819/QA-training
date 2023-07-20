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

    def get_avg_test_score(self):
        for student in self.student_list:
            print(
                f"Student name: {student.name}, AVG Test Score: {student.avg_test_score}"
            )

    def get_all_students(self):
        for student in self.student_list:
            print(f"Student: {student.name}")


# students
Mary = Student("Mary", "18")
John = Student("John", "19")
Mark = Student("Mark", "22")

# students list
students_list = [Mary, John, Mark]

# creating class
# this could be done student by student rather than using a list
new_class = Class_("Comp Sci", students_list)

# print all students
new_class.get_all_students()

# we calculate avg_test_score for one student first
# we use the class list, not the original one!
new_class.student_list[0].score1 = 10
new_class.student_list[0].score2 = 10
new_class.student_list[0].score3 = 10
new_class.student_list[0].get_avg_test_score()

new_class.get_avg_test_score()
