# ============================================
# Exercise : Student Grades Analysis
# Description:
# - Create a dictionary where keys are student names and values are grades.
# - Find the highest grade and the corresponding student.
# - Calculate the class average. - Select students with grades above 15.

# Author: Mehdi Mohammad Hashemi
# ============================================

grades = {"Ali": 18, "Sara": 12, "Reza": 16, "Neda": 19}

# بالاترین نمره
top_student = max(grades, key=grades.get)
print("Top student:", top_student, grades[top_student])

# میانگین کلاس
average = sum(grades.values()) / len(grades)
print("Class average:", average)

# دانشجویان بالای 15
above_15 = [name for name, grade in grades.items() if grade > 15]
print("Students > 15:", above_15)
