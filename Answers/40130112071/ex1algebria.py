import random

print("Hi,Wellcome to HOP GAME")
a=input()

b=random.randint(0,100)
print(b)

if type(a)==type(b) and b%a==0:
    print("It is invalid,Try again:")
    b=random.randint(0,100)
    print(b)

