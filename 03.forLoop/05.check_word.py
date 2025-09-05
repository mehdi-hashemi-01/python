# ============================================
# Exercise : Check Word
# The user inputs a word.
# Use a for loop to check if it contains "python" or not.

# کاربر یک کلمه وارد می‌کنه. با for بررسی کن آیا داخلش "python" وجود داره یا نه.

# Author: Mehdi Mohammad Hashemi
# ============================================

words = input('Enter a Sentence: ')

found = False  # Flag to track if python is found

for word in words.split():
    if word.lower() == "python":
        found = True
        break  # Stop after finding python

# Print result
if found:
    print("Yes, the word contains 'python'")
else:
    print("No, the word does not contain 'python'")






# if "python" in words.lower():
#     print("Yes, the word contains 'python'")
# else:
#     print("No, the word does not contain 'python'")