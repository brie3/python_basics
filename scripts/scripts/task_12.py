""" 
Petya and Katya are brother and sister. 
Petya is a student, and Katya is a schoolgirl. 
Petya helps Katya with math. 
He thinks of two natural numbers X and Y (X,Y≤1000), 
and Katya has to guess them. 
To do this, Petya makes two clues. 
He calls the sum of these numbers S and their product P. 
Help Katya guess numbers conceived by Petya. 
"""
print("input numbers sum")
sum = int(input())
print("input numbers product")
product = int(input())
for i in range(sum):
    for j in range(product):
        if sum == i + j and product == i * j:
            print("numbers are: ", i, j)