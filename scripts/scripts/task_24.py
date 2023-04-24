import sys
""" 
A farm in Karelia grows blueberries. 
It grows on a round bed, and the bushes are planted only around the circumference. 
Thus, each bush has exactly two neighbors. In total, N bushes grow in the garden.
These bushes have different yields, so by the time they were harvested, 
they had a different number of berries - ai berries grew on the i-th bush. 
This farm has introduced an automatic blueberry picking system. 
This system consists of a control module and several collecting modules.
The picking module in one run, being directly in front of a certain bush, 
collects berries from this bush and from two neighboring ones. 
Write a program to find the maximum number of berries that the picking module can pick in one run, 
being in front of some bush garden bed specified in the input file.
"""
def count_max():
    blueberries = list([int(x) for x in input().split()])
    if len(blueberries) == 1:
        return blueberries[0]
    if len(blueberries) == 2:
        return blueberries[0]+blueberries[1]
    if len(blueberries) == 3:
        return blueberries[0]+blueberries[1]+blueberries[2]
    max = -sys.maxsize - 1
    for i in range(-1, len(blueberries)-1):
        sum = blueberries[i-1]+blueberries[i] + blueberries[i+1]
        if sum > max:
            max = sum
    return max

print("enter number of blueberries on bushes separated by space")
print(count_max())