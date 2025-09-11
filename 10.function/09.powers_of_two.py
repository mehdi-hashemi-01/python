# Exercise : generate powers of two
# - Write a function that takes a number `n`.
# - Return a list of powers of 2 up to `n`.

# تابعی بنویس که یک عدد n بگیرد و لیست توان‌های ۲ تا n را بسازد.

# Author: Mehdi Mohammad Hashemi
# ============================================

def powers_of_two(n):
    return [2 ** i for i in range(1, n+1)]

print(powers_of_two(5))  # [2, 4, 8, 16, 32]
