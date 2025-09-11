import random as rd

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

rd.shuffle(list1)
print(list1)
rd.shuffle(list1)
print(list1)


print(rd.choice(list1))
print(rd.choice(list1))
print(rd.choice(list1))
print(rd.choice(list1))
print(rd.choices(list1,k=3))

