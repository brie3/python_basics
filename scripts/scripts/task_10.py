""" 
There are n coins on the table. 
Some of them lie tails up, and some - coat of arms. 
Determine the minimum number of coins that must be flipped 
so that all coins are turned up the same side. 
Print the minimum number of coins you need
turn over 
"""
eagles = 0
tails = 0
print("input coin count")
coins_count = int(input())
for i in range(coins_count):
    print("input next coint side: [1 - eagle, 0 - tail]")
    side = int(input())
    if side == 0:
        tails += 1
    else:
        eagles += 1

if tails > eagles:
    print("need to flip ", eagles, " eagles as minimal value to make all coins with one side.")
else:
    print("need to flip ", tails, " tails as minimal value to make all coins with one side.")