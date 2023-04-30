""" 
Determine the indices of the array (list) 
elements whose values belong to the specified range 
(i.e. not less than the specified minimum and not greater than the specified maximum)
"""
test_range = [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9]
print("enter number that represent 'min' number in range")
min_range = int(input())
print("enter number that represent 'max' number in range")
max_range = int(input())
for i in range(len(test_range)):  
    if min_range <= test_range[i] <=max_range:
        print(i)