# ============================================
# Exercise : Find Max Number
# - Write a function that takes a list of numbers.
# - Return the largest number in the list.

# تابعی بساز که یک لیست از اعداد بگیرد و بزرگ‌ترین آن را پیدا کند.

# Author: Mehdi Mohammad Hashemi
# ============================================

def find_max(numbers):
    # Assume the first number is the maximum
    maximum = numbers[0]

    # Loop through all numbers
    for num in numbers:
        # If a number is greater than the current maximum, update it
        if num > maximum:
            maximum = num

    # Return the largest number
    return maximum


print(find_max([10, 25, 7, 99, 35]))  # 99

