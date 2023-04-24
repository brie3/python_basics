""" 
Given two unordered sets of integers (maybe with repetitions). 
Print without repetitions in ascending order all those numbers that occur in both sets. 
The user enters 2 numbers. n - number of elements of the first set. 
m - number of elements of the second set. The user then enters the elements themselves.
"""
print("enter numbers of set 1")
ns = set([int(x) for x in input().split()])
print("enter numbers of set 2")
ms = set([int(x) for x in input().split()])
out = list(ns & ms)
out.sort()
for i in out:
    print(i, end=' ')