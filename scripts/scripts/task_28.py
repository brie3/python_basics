""" 
Write a recursive sum(a, b) function that returns the sum of two non-negative integers. 
Of all the arithmetic operations, only +1 and -1 are allowed. You can't use loops either.
"""

def sum(a,b):
    if b < 1:
        return a
    return 1+sum(a,b-1)

def fibo(n):
    if n <= 1:
        return 1
    return fibo(n-1)+fibo(n-2)

print(sum(2,5))
print(fibo(5))