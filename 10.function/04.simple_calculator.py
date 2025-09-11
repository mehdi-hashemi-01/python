# ============================================
# Exercise : Simple Calculator
# - Write four separate functions: `add`, `subtract`, `multiply`, `divide`.
# - Then write a main function `calculator(operation, a, b)` that calls the right function based on the operation.

# چهار تابع جدا بنویس: جمع، تفریق، ضرب، تقسیم.
# بعد یک تابع کلی بساز که عملیات و دو عدد بگیرد و نتیجه را بدهد.

# Author: Mehdi Mohammad Hashemi
# ============================================

def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b if b != 0 else "خطا: تقسیم بر صفر!"

def calculator(a, b, op):
    if op == "+": return add(a, b)
    if op == "-": return subtract(a, b)
    if op == "*": return multiply(a, b)
    if op == "/": return divide(a, b)
    return "عملیات نامعتبر!"

print(calculator(10, 5, "+"))  # 15
