# ============================================
# Exercise : Inventory Management
# Description:
# - Create a dictionary where product name = key, stock quantity = value.
# - Add or update stock for a product.
# - Remove a product.
# - Calculate the total stock quantity.

# Author: Mehdi Mohammad Hashemi
# ============================================

inventory = {"laptop": 10, "mouse": 25, "keyboard": 15}

inventory["mouse"] = 30   # بروزرسانی
inventory["monitor"] = 5  # اضافه کردن

inventory.pop("keyboard")  # حذف محصول

total_stock = sum(inventory.values())
print("Total stock:", total_stock)
print(inventory)
