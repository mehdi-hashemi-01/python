# ============================================
# Exercise : Calculate Average Grade
# - Write a function that takes a list of student grades.
# - Calculate the average.
# - Return both the average and the pass/fail status (pass if average ≥ 10).

# تابعی بنویس که لیست نمرات دانشجو را بگیرد، معدل حساب کند و وضعیت قبولی/ردی را برگرداند.

# Author: Mehdi Mohammad Hashemi
# ============================================

# Define a function to calculate average grade
def calculate_average_grade(grades):
    # Calculate average by dividing sum by number of grades
    average = sum(grades) / len(grades)

    # status = "pass" if average >= 10 else "fail"
    # return average, status

    # Check if average is greater than or equal to 10
    if average >= 10:
        return "pass"
    else:
        return "fail"


# Test the function with a list of grades
print(calculate_average_grade([11, 20, 13, 14, 15, 16, 17, 8, 9]))



