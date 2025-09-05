# ============================================
# Exercise : Pass Fail Count
# A class has scores: [18, 7, 12, 20, 15].
# Use a for loop to count how many students passed (score > 10) and how many failed.

# یه کلاس داری با نمره‌های [18, 7, 12, 20, 15]. با for تعداد قبولی‌ها (نمره بالای 10) و تعداد مردودی‌ها رو بشمار.

# Author: Mehdi Mohammad Hashemi
# ============================================

# List of student scores
list1 = [18, 7, 12, 20, 15]

# Initialize counters
passed = 0
failed = 0

# Loop through each score
for i in list1:
    # If score is greater than 10 → student passed
    if i > 10:
        passed += 1
    # Otherwise → student failed
    else:
        failed += 1

# Print the results
print(f"Passed: {passed}")
print(f"Failed: {failed}")



# Calculate total students
# total_students = len(list1)

# Calculate passing percentage
# passing_percentage = (passed / total_students) * 100

# Print the results
# print(f"Passing Percentage: {passing_percentage:.2f}%")
