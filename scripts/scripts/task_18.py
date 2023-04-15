import sys
""" 
It is required to find in the array A[N] 
the closest element in size to the given number X. 
In the first line, the user enters a natural number N, 
the number of elements in the array.
The next lines contain N integers Ai. The last line contains the number X
"""
print("input N that represent array length")
N = int(input())
numbers = []
for i in range(N):
    numbers.append(int(input()))

print("input num to find closest in array")
needle = int(input())

diff = sys.maxsize
number = 0
for i in numbers:
    if diff > abs(needle - i):
        diff = abs(needle - i) 
        number = i
print("number ", number, " closest in array to ", needle)