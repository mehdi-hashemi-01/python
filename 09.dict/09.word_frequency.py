# ============================================
# Exercise : Word Frequency
# Description:
# - Take a short text.
# - Create a dictionary where keys = words, values = word count.
# - Find the most frequent word.
# - Print the unique words.

# Author: Mehdi Mohammad Hashemi
# ============================================

text = "python is fun and python is powerful and python is easy"
words = text.split()

freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1

print(freq)

# بیشترین تکرار
most_frequent = max(freq, key=freq.get)
print("Most frequent word:", most_frequent)

# کلمات یکتا
print("Unique words:", list(freq.keys()))
