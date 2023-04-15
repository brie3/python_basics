import sys
""" 
Problem 20: In the board game Scrabble, each letter has a certain value.
In the case of the English alphabet, points are distributed as follows: A, E, I, O, U, L, N, S, T, R - 1 point; D, G - 2 points; B, C, M, P - 3 points;
F, H, V, W, Y - 4 points; K - 5 points; J, X - 8 points; Q, Z - 10 points.
Write a program that calculates the cost of a word entered by the user. We will assume that only one word is given as input,
which contains either only English letters.
"""
eng_alph = {
    'A': 1, 'a': 1,
    'B': 3, 'b': 3,
    'C': 3, 'c': 3,
    'D': 2, 'd': 2,
    'E': 1, 'e': 1,
    'F': 4, 'f': 4,
    'G': 2, 'g': 2,
    'H': 4, 'h': 4,
    'I': 1, 'i': 1,
    'J': 8, 'j': 8,
    'K': 2, 'k': 2,
    'L': 2, 'l': 2,
    'M': 3, 'm': 3,
    'N': 1, 'n': 1,
    'O': 1, 'o': 1,
    'P': 1, 'p': 1,
    'Q': 10, 'q': 10,
    'R': 1, 'r': 1,
    'S': 1, 's': 1,
    'T': 1, 't': 1,
    'U': 1, 'u': 1,
    'V': 4, 'v': 4,
    'W': 4, 'w': 4,
    'X': 8, 'x': 8,
    'Y': 4, 'y': 4,
    'Z': 10, 'z': 10,
}
print("enter word")
word = str(input())
sum = 0
for i in word:
    sum += eng_alph[i]

print("scrabble word value is: ", sum)