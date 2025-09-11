# Exercise : calculate game score
# - Game rules:
#   - Win = +3 points
#   - Draw = +1 point
#   - Loss = 0
# - Write a function that takes number of wins, draws, and losses.
# - Return the total score.

# یک بازی فرضی داریم. قوانین امتیاز:
# •	هر برد: +3 امتیاز
# •	هر مساوی: +1 امتیاز
# •	هر باخت: +0
# تابعی بنویس که تعداد برد، مساوی و باخت را بگیرد و امتیاز نهایی را حساب کند.

# Author: Mehdi Mohammad Hashemi
# ============================================

# Calculate total game points based on wins, draws, and losses
def game_points(wins, draws, losses):
    # Each win = 3 points, each draw = 1 point
    return (wins * 3) + (draws * 1)

# Test the function
print(game_points(3, 2, 1))  # 11
