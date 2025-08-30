def calculate_average(scores):
    if len(scores) == 0:
        return 0
    return sum(scores) / len(scores)

# Dictionary to store student names and their scores
student_scores = {
    "Alice": [85, 90, 78],
    "Bob": [70, 88, 92],
    "Charlie": [95, 80, 85]
}

# Display student scores
print("Student Scores:")
for student, scores in student_scores.items():
    print(f"{student}: {scores} (Average: {calculate_average(scores):.2f})")

# Adding a new student
student_scores["David"] = [88, 76, 90]

print("\nAfter adding David:")
for student, scores in student_scores.items():
    print(f"{student}: {scores} (Average: {calculate_average(scores):.2f})")
