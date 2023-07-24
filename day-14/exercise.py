"""
In a new Python file, create a class of students.
It should contain the following attributes: name, age, and class with default value "student".

It should also contain a method which takes in 3 test scores and prints the students average test score.
"""

# imports
from tutorial import Student


class Class_:
    """Class to manage a group of students, made using Student instances."""

    def __init__(self, class_name: str, student_list: list[Student]) -> None:
        """Initialise Class

        Args:
            class_name (str): Name of the class
            student_list (list): List of Student instances
        """
        self.class_name = class_name
        self.student_list = student_list

    def get_avg_test_score(
        self, student: Student, score1: float, score2: float, score3: float
    ) -> None:
        """Return average test score of a particular student

        Args:
            student (Student): Student to compute the average test score of
            score1 (float): Score of test 1
            score2 (float): Score of test 2
            score3 (float): Score of test 3
        """
        print(
            f"Student name: {student.name}, AVG Test Score: {student.compute_avg_test_score(score1, score2, score3)}"
        )

    def get_all_students(self) -> None:
        """Print all Students"""
        for student in self.student_list:
            print(f"Student: {student}")


if __name__ == "__main__":
    # students
    Mary = Student("Mary", "18")
    John = Student("John", "19")
    Mark = Student("Mark", "22")

    # students list
    students_list = [Mary, John, Mark]

    # creating class
    # this could be done student by student rather than using a list (add to class method best way probably)
    new_class = Class_("Comp Sci", students_list)

    # print all students
    new_class.get_all_students()

    # calculate avg_test_score
    new_class.get_avg_test_score(Mary, 10, 10, 10)
    new_class.get_avg_test_score(John, 20, 20, 20)
    new_class.get_avg_test_score(Mark, 40, 40, 40)
