import numpy as np
print("===== STUDENT MARKS ANALYZER =====\n")

# Student names
students = np.array([
    "Aneeqa",
    "Sara",
    "Ali",
    "Zoya",
    "Ahmed",
    "Fatima",
    "Noor",
    "Hassan"
])

# Student marks
marks = np.array([95, 88, 91, 72, 65, 84, 97, 78])

print("Student Names:")
print(students)
print("Student's Marks:")
print(marks)

print("Highest Marks:", marks.max())
print("Lowest Marks:", marks.min())
print("Average Marks:", marks.mean())

print("Students Scoring 90 or Above:")
print(marks[marks >= 90])
print("Students Below Average:")

print(marks[marks < marks.mean()])
print("Number of Students:", len(marks))

topper_index = marks.argmax()
print("Topper:", students[topper_index])

lowest_index = marks.argmin()
print("Lowest Scorer:", students[lowest_index])

print("\n--- REPORT SUMMARY ---")
print("Topper:", students[marks.argmax()])
print("Highest Marks:", marks.max())
print("Class Average:", marks.mean())
print("Total Students:", len(marks))
