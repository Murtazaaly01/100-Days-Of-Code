num1 = int(input("Enter Number 1 : "))
num2 = int(input("Enter Number 2 : "))
num3 = int(input("Enter Number 3 : "))
num4 = int(input("Enter Number 4 : "))

f1 = max(num1, num4)
f2 = max(num2, num3)
if (f1>f2):
    print(f"{str(f1)}is greatest")
else:
    print(f"{str(f2)}is greatest")
