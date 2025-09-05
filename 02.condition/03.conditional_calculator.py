# ============================================
# Exercise : Conditional Calculator
# Description: Write a program that takes two numbers and an operator (+, -, *, /), then prints the result.

# برنامه‌ای بنویس که دو عدد و یک عملگر (+ , - , * , /) بگیرد و جواب را چاپ کند.

# Author: Mehdi Mohammad Hashemi
# ============================================

# Ask the user to enter the first number
num1 = int(input('Enter first number: '))

# Ask the user to enter the second number
num2 = int(input('Enter second number: '))

# Ask the user to enter an operator (+, -, *, /)
operator = input('Enter operator: ')

# Perform calculation based on operator
if operator == '+':
    print(num1 + num2)
elif operator == '-':
    print(num1 - num2)
elif operator == '*':
    print(num1 * num2)
elif operator == '/':
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Error: Division by zero is not allowed!")
else:
    print("Invalid operator entered!")

