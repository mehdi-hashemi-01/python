# ============================================
# Exercise : Compare Numbers
# Description: Take two numbers and print which one is larger. If they are equal, print that as well.

#  دو عدد بگیر و چاپ کن کدام بزرگ‌تر است. اگر مساوی بودند هم اعلام کن.

# Author: Mehdi Mohammad Hashemi
# ============================================

# Ask the user to enter the first number
number1 = int(input('Enter first number: '))

# Ask the user to enter the second number
number2 = int(input('Enter second number: '))

# Check if the numbers are equal
if number1 == number2:
    print(number1, 'and', number2, 'are equal')

# Check if the first number is greater
elif number1 > number2:
    print(number1, 'is greater than', number2)

# Otherwise, the second number is greater
else:
    print(number2, 'is greater than', number1)
