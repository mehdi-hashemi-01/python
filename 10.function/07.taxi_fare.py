# ============================================
# Exercise : Taxi Fare
# - Write a function that takes kilometers traveled.
# - Formula: 10,000 fixed + 2,500 per km.
# - Return the total fare.

# تابعی بنویس که بر اساس کیلومتر طی‌شده، هزینه تاکسی را حساب کند.
# •	ورودی: کیلومتر طی‌شده
# •	هزینه: 10,000 تومان ورودی ثابت + 2,500 تومان به ازای هر کیلومتر

# Author: Mehdi Mohammad Hashemi
# ============================================

# Define a function to calculate taxi fare
def taxi_fare(km):
    # Base fare is 10,000 plus 2,500 per kilometer
    return 10000 + (2500 * km)

# Test the function
print(taxi_fare(5))  # Output: 22500
