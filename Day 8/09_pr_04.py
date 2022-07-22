# n! = (n-1)! * n 
# sum(n) = sum(n-1) + n

def recur_sum(n):
   return n if n <= 1 else n + recur_sum(n-1)

d = recur_sum(5)
print(d)    