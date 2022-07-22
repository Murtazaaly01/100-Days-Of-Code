num = int(input("Enter Your Number: "))
prime = all(num%1 != 0 for _ in range(2, num))
if prime:
    print("Number Is Prime")
else:
    print("Number Is Not Prime")     