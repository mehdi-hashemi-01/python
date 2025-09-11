# Exercise : calculate Calories
# - Write a function that takes a list of food names.
# - Use predefined calories: burger=500, pizza=600, salad=200, fries=300.
# - Return the total calories.

# تابعی بساز که اسم غذاها را بگیرد و کالری کل را حساب کند.
# •	فرضی: همبرگر=500، پیتزا=600، سالاد=200، سیب‌زمینی=300

# Author: Mehdi Mohammad Hashemi
# ============================================


# Define a dictionary of food calories
calories_dict = {"burger": 500, "pizza": 600, "salad": 200, "fries": 300}

def calories(foods):
    total = 0
    # Loop through each food and add its calories
    for food in foods:
        total += calories_dict.get(food, 0)
    return total

# Test the function
print(calories(["burger", "salad", "fries"]))  # 1000
