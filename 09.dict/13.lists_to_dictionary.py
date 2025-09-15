# ============================================
# Exercise : Lists To Dictionary
# Description:
# - Create two lists:
# keys = ["name","age","city"]
# values = ["Ali", 25, "Tehran"]
# - Convert them into a dictionary.
# - Update the value of the key "city".

# Author: Mehdi Mohammad Hashemi
# ============================================

keys = ["name", "age", "city"]
values = ["Ali", 25, "Tehran"]

person = dict(zip(keys, values))
print(person)

# بروزرسانی
person["city"] = "Shiraz"
print(person)
