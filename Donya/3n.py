# 3-D array animation in plain terminal
import numpy as np
import time
import os

# ------------------ ساخت داده ------------------
cube = np.random.randint(10, 99, size=(2, 3, 4))   # 2 لایه، 3 سطر، 4 ستون

# ------------------ تابع پاک‌کننده صفحه ---------
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# ------------------ انیمیشن ----------------------
for depth in range(cube.shape[0]):          # برای هر لایه
    clear()
    print(f"📄  لایه {depth} از {cube.shape[0]-1}\n")
    for row in cube[depth]:                 # چاپ سطرهای همان لایه
        print(' '.join(f"{col:2}" for col in row))
    time.sleep(2.2)                         # سرعت ورق‌خوردن (ثانیه)

print("\n✅ تمام!")