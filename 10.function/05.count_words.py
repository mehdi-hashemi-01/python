# ============================================
# Exercise : Count Words
# - Write a function that takes a text string.
# - Return the number of words in the text.

# تابعی بنویس که یک متن بگیرد و تعداد کلمات آن را حساب کند.

# Author: Mehdi Mohammad Hashemi
# ============================================

# Define a function to count words in a text
def count_words(text):
    # Split the text by spaces and count the number of items
    return len(text.split())

# Test the function
print(count_words("Hello World"))  # Output: 2
