# ============================================
# Exercise : Compare Two Dictionaries
# Description:
# - Create two dictionaries containing exam scores:
# exam1 = {"Ali": 18, "Sara": 15, "Reza": 12}
# exam2 = {"Ali": 20, "Sara": 14, "Reza": 12}
# - Print students who scored above 15 in both exams.
# - Print students whose scores have changed.

# Author: Mehdi Mohammad Hashemi
# ============================================

exam1 = {"Ali": 18, "Sara": 15, "Reza": 12}
exam2 = {"Ali": 20, "Sara": 14, "Reza": 12}

# دانشجویان بالای 15 در هر دو امتحان
above_15 = [name for name in exam1 if exam1[name] > 15 and exam2[name] > 15]
print("Above 15 in both exams:", above_15)

# تغییر نمره‌ها
changed = [name for name in exam1 if exam1[name] != exam2[name]]
print("Scores changed:", changed)
