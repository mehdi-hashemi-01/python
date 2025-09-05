# ============================================
# Exercise : Even Or Odd
# Description: Take a number and print whether it is even or odd.

# یک عدد بگیر و بگو زوج است یا فرد.

# Author: Mehdi Mohammad Hashemi
# ============================================

# Ask the user to enter a number
num = int(input("Enter a number: "))

# Check if the number is divisible by 2
if num % 2 == 0:
    print("Even")   # If divisible, it's even
else:
    print("Odd")    # Otherwise, it's odd
