# ============================================
# Exercise : Check Palindrome
# - Write a function that checks if a word is a palindrome (the same forwards and backwards).
# تابعی بساز که بررسی کند آیا یک کلمه از دو طرف یکسان است یا نه.

# Author: Mehdi Mohammad Hashemi
# ============================================

def is_palindrome(word):
    # Convert to lowercase before checking
    word = word.lower()
    return word == word[::-1]

# Test cases
print(is_palindrome("PoP"))   # True
print(is_palindrome("Level")) # True
print(is_palindrome("Hello")) # False
