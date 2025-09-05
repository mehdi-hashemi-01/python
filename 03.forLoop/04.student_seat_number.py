# ============================================
# Exercise : Student Seat Number
# List of student names: ["Ali", "Sara", "Reza"].
# Use a for loop to assign each name a seat number and print it (e.g., Ali → Seat 1).

# لیست اسم‌ دانشجوها: ["Ali", "Sara", "Reza"]. با for به هر اسم یک شماره‌ی صندلی بده و چاپ کن (مثلاً Ali → صندلی 1).

# Author: Mehdi Mohammad Hashemi
# ============================================


# List of student names
students = ["Ali", "Sara", "Reza"]

for i in range(len(students)):
    # Print student name with seat number (i+1 to start from Seat 1)
    print(f"{students[i]} → Seat {i+1}")



# Loop through the list with index using enumerate
# for index, name in enumerate(students, start=1):
    # Print student name with seat number
    # print(f"{name} → Seat {index}")