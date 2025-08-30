# ============================================
# Exercise : Class Members Set
# Description:
# - Create a set containing the names of many students in a class.
# - Print the length of the set (unique students count).
# - Add a new student to the set.

# •	یک مجموعه بساز که شامل نام تعدادی دانش‌آموزان کلاس باشد.
# •	طول مجموعه را چاپ کن تا تعداد دانش‌آموزان یکتا را ببینی.
# •	یک دانش‌آموز جدید به مجموعه اضافه کن.

# Author: Mehdi Mohammad Hashemi
# ============================================

# Create a set of students in the class
students = {'Ali', 'Mehdi', 'Hosein', 'Amir', 'Nima', 'Mohammad', 'Amin' }

# Print the number of unique students
print("Number of unique students:",len(students))

# Add a new student to the set
students.add("Ahmad")
print("Updated students set:", students)