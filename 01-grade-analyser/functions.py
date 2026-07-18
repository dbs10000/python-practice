# functions.py

def calculate_average(student_grades):
    num_of_students = 0
    total_scores = 0
    
    for student in student_grades.keys():
        # print(f"student: {student}")
        num_of_students += 1
    
    for student in student_grades.values():
        # print(f"student: {student}")
        total_scores += student
    
    # print(f"num_of_students: {num_of_students}")
    # print(f"total_scores: {total_scores}")
    average_score = total_scores / num_of_students

    print(f"Class Average: {average_score}%")


def top_performer(student_grades):
    grade = 0
    for name, score in student_grades.items():
        # print(f"name: {name}")
        # print(f"score: {score}")
        if score > grade:
            grade = score
        # print(f"grade: {grade}")
    for name, score in student_grades.items():
        if score == grade:
            print(f"Top Performer: {name} with a score of {score}")
