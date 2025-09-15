# ============================================
# Exercise : User Data Analysis
# Description:
# - Create a dictionary with usernames as keys and their interests as values (list).
# Example: {"Alice": ["music","reading"], "Bob": ["movies","music"]}
# - Find interests common to all users.
# - Print the number of interests for each user.

# Author: Mehdi Mohammad Hashemi
# ============================================

users = {
    "Alice": ["music", "reading", "movies"],
    "Bob": ["movies", "music"],
    "Charlie": ["music", "travel", "movies"]
}

# علایق مشترک
common = set(users["Alice"])
for interests in users.values():
    common &= set(interests)
print("Common interests:", common)

# تعداد علاقه‌ها
for user, interests in users.items():
    print(user, "has", len(interests), "interests")
