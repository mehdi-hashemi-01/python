# ============================================
# Exercise : Taxi Fare
# Description:
# If the distance is less than 5 km → fare = 20,000
# If between 5 and 10 km → fare = 35,000
# If more than 10 km → fare = 50,000

# اگر مسافت کمتر از ۵ کیلومتر بود → هزینه = ۲۰،۰۰۰
# اگر بین ۵ تا ۱۰ کیلومتر → هزینه = ۳۵،۰۰۰
# اگر بیشتر از ۱۰ کیلومتر → هزینه = ۵۰،۰۰۰

# Author: Mehdi Mohammad Hashemi
# ============================================

# Ask the user to enter the distance in kilometers
distance = float(input("Enter distance in kilometers: "))

# Calculate the cost based on distance
if distance < 5:
    cost = 20000
elif 5 <= distance <= 10:   # between 5 and 10
    cost = 35000
else:                  # more than 10
    cost = 50000

# Print the result
print("The cost is:", cost)
