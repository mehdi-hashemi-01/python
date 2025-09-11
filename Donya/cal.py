a=int(input("Enter a number:"))
b=int(input("Enter another number:"))
operator=input("Enter operator:")


def add(x, y):
    print(x + y)
def sub(x, y):
    print(x - y)
def mul(x, y):
    print(x * y)
def div(x, y):
    print(x / y)


if operator=="+":
    add(a,b)
elif operator=="-":
    sub(a,b)
elif operator=="*":
     mul(a,b)
elif operator=="/":
    if b==0:
        print("zero div")
    else:
        div(a,b)
else:
     print("Invalid operator")


