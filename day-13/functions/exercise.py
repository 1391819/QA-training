"""
Create a program that works out a grade based on 
marks with the use of functions.

The program should take the 
    - students name, 
    - homework score (/25), 
    - assessment score (/50) 
    - and final exam score (/100) as inputs, 
    
and output 
    - their name 
    - and final ICT grade as a percentage.

Reminder: 
any inputs and prints should not be included inside the 
function definition, and should strictly be done outside.

Stretch goal: 
Include grade boundaries such that the program also 
outputs a grade for the student (A, B, etc.)
"""


# calculating final ICT grade as a percentage
# student_name: student name
# homework_score: homework score (out of 25)
# assessment_score: assessment score (out of 50)
# final_exam_score: final exam score (out of 100)
# return: student_name, final mark (percentage), grade boundary
def calculate_mark(student_name, homework_score, assessment_score, final_exam_score):
    # sum of all scores
    total_score = homework_score + assessment_score + final_exam_score
    # calculating the percentage
    percentage = (total_score / 175) * 100

    if percentage >= 90:
        grade_boundary = "A"
    elif percentage >= 80:
        grade_boundary = "B"
    elif percentage >= 70:
        grade_boundary = "C"
    elif percentage >= 60:
        grade_boundary = "D"
    else:
        grade_boundary = "F"

    return student_name, percentage, grade_boundary


# getting user input
student_name = input("Enter student name: ")
homework_score = float(input("Enter homework score: "))
assessment_score = float(input("Enter assessment score: "))
final_exam_score = float(input("Enter final exam score: "))

# calculating mark and retrieving needed data for output
student_name, percentage, final_mark = calculate_mark(
    student_name, homework_score, assessment_score, final_exam_score
)

# printing
print(f"Student name: {student_name}")
print(f"Final mark: {percentage}%")
print(f"Final grade: {final_mark}")
