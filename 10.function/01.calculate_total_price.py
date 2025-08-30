# ============================================
# Exercise : Calculate the Total Purchase Price
# Description: This program takes a list of item prices and calculates their total.

#  محاسبه مجموع قیمت خرید
# توضیح: این برنامه لیستی از قیمت کالاها را می‌گیرد و مجموع آن‌ها را حساب می‌کند.

# Author: Mehdi Mohammad Hashemi
# ============================================

def calculate_total_price(list_price):
    return sum(list_price)


# Usage
total_price = calculate_total_price([1200, 3700, 52700, 26800, 94100])
print(f"Total Price: {total_price}")