# ============================================
# Exercise : Currency Conversion
# Description: Have one variable for the amount in dollars and another for the conversion rate from dollar to toman.
# Calculate the amount in tomans.

# یک متغیر برای مقدار دلار و یک متغیر برای نرخ تبدیل دلار به تومان داشته باش. مقدار تومان را حساب کن.

# Author: Mehdi Mohammad Hashemi
# ============================================

# Ask the user to enter the amount in dollars
amount_in_dollars = float(input("Enter amount in dollars: "))

# Ask the user to enter the conversion rate (1 dollar = ? tomans)
rate = float(input("Enter conversion rate (dollar to toman) - > (1 dollar = ? tomans): "))

# Calculate amount in tomans (dollars × rate)
amount_in_tomans = amount_in_dollars * rate

# Print the result
print("Amount in tomans:", amount_in_tomans)
