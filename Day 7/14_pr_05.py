num = int(input("Enter Your Number: "))

factorial = 0
for i in range(1, num + 1):
    factorial = factorial*i
print(f"Factorial of {num} is {factorial}")