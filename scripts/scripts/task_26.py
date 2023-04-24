""" 
Calculate factorial (product of 1 to N) and 
triangular number (sum of numbers from 1 to N) 
for the number N VIA RECURSION and without loops.
"""

def factorial(n):
    if n < 1:
        return 1
    return n * factorial(n-1)

def triangular(n):
    if n < 1:
        return 0
    return n + triangular(n-1)

print(factorial(5))
print(triangular(5))