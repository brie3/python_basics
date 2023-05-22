""" 
Winnie the Pooh asked you to see if there is a rhythm in his poems. 
Since his chants are not as easy to understand as he makes them easy to understand, 
you should write a program. Winnie the Pooh believes that there is a rhythm 
if the number of syllables (i.e. the number of vowels) in each phrase of the poem is the same.

A phrase can consist of one word, if there are several words in the phrase, 
then they are separated by hyphens. 
Phrases are separated from each other by spaces. 
Poem Winnie the Pooh drives into the program from the keyboard.
In response, write “Param pam-pam” if the rhythm is okay and “Pam param” if the rhythm is not okay.

**Input:** para-ra-ram ram-pam-papam pa-ra-pa-da
**Output:** Param pam pam
"""
syllables = input("enter phrase\n").replace("-", "").split()

def countVowels(word):
    sum = 0
    for i in word:
        if i.lower() in "aeiou":
            sum +=1
    return sum 

def verdict(sums):
    if len(sums) < 2:
        return "Pam param"
    i = sums[0]
    for j in sums[1:]:
        if i != j:
            return "Pam param" 
    return "Param pam pam"

print(verdict(list(map(countVowels, syllables))))