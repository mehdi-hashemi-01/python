# ============================================
# Exercise : Countries List
# Description:
# - Create an empty list called `countries`.
# - Add at least 6 different countries to the list.
# - Print the total number of countries.
# - Print the first country, the middle country, and the last country.

# یک لیست خالی به نام countries  بساز و سپس حداقل ۶ کشور مختلف به آن اضافه کن.

# 1.	تعداد کل کشورها در لیست را چاپ کن.
# 2.	اولین کشور، کشور وسطی و آخرین کشور را چاپ کن.

# Author: Mehdi Mohammad Hashemi
# ============================================

# Create an empty list
countries = []

countries.extend(['Iran', 'Germany', 'Japan', 'Brazil'])

# Add countries one by one using append
countries.append('Canada')     # Add Canada
countries.append('Australia')  # Add Australia

# Print the total number of countries
print("Number of countries:", len(countries))

# Print the first, middle, and last country
first_country = countries[0]               # First country
middle_country = countries[len(countries)//2]  # Middle country
last_country = countries[-1]               # Last country

print("First country:", first_country)
print("Middle country:", middle_country)
print("Last country:", last_country)
