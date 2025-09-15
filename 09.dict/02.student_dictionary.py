# ============================================
# Exercise : Student Dictionary
# Description:
# - Create a dictionary with the following
# keys: first_name, last_name, gender, age, marital_status, skills, country, city, address
# - Add multiple skills, e.g., ["frontend", "database design", "CSS"].
# - Print the dictionary.

# Author: Mehdi Mohammad Hashemi
# ============================================

student = {
    "first_name": "Mehdi",
    "last_name": "Hashemi",
    "gender": "Male",
    "age": 21,
    "marital_status": "Single",
    "skills": ["frontend", "database design", "CSS"],
    "country": "Iran",
    "city": "Kerman",
    "address": "Valiasr St"
}
print(student)


print(len(student))  # تعداد کل کلیدها
print(student["skills"])  # نمایش مهارت‌ها
print(type(student["skills"]))  # نوع داده


student["skills"].append("Python")
student["skills"].append("Git")

print(list(student.keys()))    # کلیدها
print(list(student.values()))  # مقادیر


student_items = list(student.items())
print(student_items)


student.pop("last_name")  # حذف کلید
print(student)

del student  # حذف کامل دیکشنری
