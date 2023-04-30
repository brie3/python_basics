""" 
Fill the array with the elements of an arithmetic progression. 
It's the first element, the difference and the number of elements must be entered from the keyboard.
The formula for getting the nth member of the progression is: an = a1 + (n-1) * d.
Each number is entered on a new line.
"""
print("enter number that represent 'a1'")
a1 = int(input())
print("enter number that represent 'd'")
d = int(input())
print("enter number that represent 'n'")
n = int(input())
for i in range(n):  
    print(a1 + i * d)