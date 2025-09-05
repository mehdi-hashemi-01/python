# ============================================
# Exercise : Total Prices
# List of product prices: [12000, 35000, 8000, 15000].
# Use a for loop to calculate the total purchase amount.

# لیست قیمت محصولات  [12000, 35000, 8000, 15000]. با  for مجموع کل خرید رو حساب کن.

# Author: Mehdi Mohammad Hashemi
# ============================================

# List of product prices
list1 = [12000, 35000, 8000, 15000]

# Initialize total sum to 0
sum = 0

# Iterate through each price in the list
for i in list1:
    # Add the current price to the total sum
    sum = sum + i

# Print the final total purchase amount

print("Total purchase amount is:", sum)



# List of product prices
# list1 = [12000, 35000, 8000, 15000]

# Use the built-in sum() function to calculate the total
# total = sum(list1)

# Print the final total purchase amount with text
# print("Total purchase amount is:", total, "Toman")
