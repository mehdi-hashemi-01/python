# ============================================
# Exercise : Temperature Conversion
# Description: Take the variable `celsius` and convert it to Fahrenheit.
# Formula: F = C * 1.8 + 32

#  متغیر celsius  را بگیر و دمای آن را به فارنهایت تبدیل کن.
# فرمول: F = C * 1.8 + 32

# Author: Mehdi Mohammad Hashemi
# ============================================

# Ask the user to enter temperature in Celsius and convert it to float
celsius = float(input("Enter temperature in Celsius: "))

# Convert Celsius to Fahrenheit using the formula (°C × 1.8) + 32
fahrenheit = 1.8 * celsius + 32

# Print the result
print(fahrenheit)
