class Student:
    """
    Student class used to track name, age, and the average test score
    """

    def __init__(self, name: str, age: int) -> None:
        """Initialise student instance

        Args:
            name (str): Name of the student
            age (int): Age of the student
        """
        self.name = name
        self.age = age
        self.avg_test_score = 0

    def compute_avg_test_score(
        self, score1: float, score2: float, score3: float
    ) -> None:
        """Compute the student average test score

        Args:
            score1 (float): Score of test 1
            score2 (float): Score of test 2
            score3 (float): Score of test 3

        Returns:
            float: Average of test scores
        """
        self.avg_test_score = (score1 + score2 + score3) / 3
        return self.avg_test_score

    def __str__(self):
        return (
            f"Name: {self.name}, Age: {self.age}, Avg Test Score: {self.avg_test_score}"
        )
