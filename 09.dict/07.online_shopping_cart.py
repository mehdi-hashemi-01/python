# ============================================
# Exercise : Online Shopping Cart
# Description:
# - Create a dictionary of products with their prices, e.g.: {"milk": 5000, "bread": 3000, "egg": 1000}
# - Calculate the total price of products.
# - Add a new product with price. - Remove one product.

# Author: Mehdi Mohammad Hashemi
# ============================================

cart = {"milk": 5000, "bread": 3000, "egg": 1000}
total = sum(cart.values())
print("Total price:", total)

cart["butter"] = 7000  # اضافه کردن محصول جدید
cart.pop("egg")        # حذف محصول

print(cart)
