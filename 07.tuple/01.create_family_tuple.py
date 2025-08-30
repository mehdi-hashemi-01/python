# ============================================
# Exercise : Create Family Tuple
# Description:
# - Create a tuple containing the names of your brothers and sisters.
# - Print the number of members in the tuple.
# - Combine all members into a new tuple named `family_members`.

# •	یک Tuple بساز که شامل اسامی برادرها و خواهرها باشد.
# •	تعداد اعضای Tuple را چاپ کن.
# •	اعضای Tuple را با هم ترکیب کن و در یک Tuple جدید به نام  family_members ذخیره کن.

# Author: Mehdi Mohammad Hashemi
# ============================================

# Create Tuples for brothers and sisters
brothers = ("Ali", "Reza", "Sami")
sisters = ("Sara", "Neda")

# Print the number of members in each Tuple
print("Number of brothers:", len(brothers))
print("Number of sisters:", len(sisters))

# Combine the members into a new Tuple
family_members = brothers + sisters
print("Family members:", family_members)
print("Total number of family members:", len(family_members))
