def maximum(num1,num2,num3):
    if (num1>num2):
        return num1
    else:
        return num2 if (num2>num3) else num3        

m = maximum(3,67,899)
print("The value of the maximum is", m)