""" 
Problem 16: It is required to calculate 
how many times some number X occurs in the array A[N]. 
The user in the first line enters a natural number N - the number of elements in the array. 
The next lines contain N integers Ai. The last line contains the number X
"""
print("input N that represent array length")
N = int(input())
numbers = []
for i in range(N):
    numbers.append(int(input()))

print("input num to find how may times it occurs in the array")
needle = int(input())

sum = 0
for i in numbers:
    if i == needle:
        sum += 1
print("number ", needle, " occurs in array ", sum," times")