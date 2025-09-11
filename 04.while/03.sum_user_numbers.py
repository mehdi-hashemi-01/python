# ============================================
# Exercise : Sum User Numbers
# The user enters several numbers.
# Stop the loop when a negative number is entered and print the sum of the positive numbers.

# کاربر چندتا عدد وارد می‌کنه. وقتی عدد منفی وارد شد، حلقه متوقف بشه و مجموع اعداد مثبت چاپ بشه.

# Author: Mehdi Mohammad Hashemi
# ============================================

# Initialize sum to 0
sum = 0

# Infinite loop to continuously ask the user for numbers
while True:
    # Ask the user to enter a number
    user_input = int(input("Enter a number: "))

    # If the number is negative, exit the loop
    if user_input < 0:
        break

    # Add the entered number to the sum
    sum += user_input

# Print the final sum
print(f"The sum is: {sum}")
