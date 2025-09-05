# ============================================
# Exercise : Countdown
# Ask the user for a number.
# Use a while loop to count down from that number to 1.

# یک عدد از کاربر بگیر. با while  از اون عدد تا 1 شمارش معکوس کن.

# Author: Mehdi Mohammad Hashemi
# ============================================

# Ask the user to enter a number
number = int(input("Enter a number: "))

# Loop while number is greater than 0
while number > 0:
    # Print the current number
    print(number)

    # Decrease the number by 1
    number -= 1
