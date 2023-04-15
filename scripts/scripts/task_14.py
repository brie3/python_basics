""" 
It is required to print all integer powers of two 
(that is, numbers of the form 2k) that do not exceed N. 
"""
print("input N")
N = int(input())
numbers = []
for i in range(N):
    pows = 2 ** i
    if pows > N:
        break
    numbers.append(pows)
print(numbers)