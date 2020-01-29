#In challenge9.py,
#Write a function that takes a string input, and returns the first character that is not repeated anywhere in the string.
#For example, if given the input 'stress', the function should return 't', since the letter t only occurs once in the 
#string, and occurs first in the string.
#As an added challenge, upper- and lowercase letters are considered the same character, but the function should return the 
#correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.
#If a string contains all repeating characters, it should return an empty string ("").
#Example:
#challenge12.py  "stress"
#Output:
#"T"
#Example:
#challenge12.py "abba"
#Output
#""
import sys
def nonRepeatingCharacter(someStr):
    order = []
    counts = {}
    items = 0
    for letter in someStr:
        if letter in counts or letter.lower() in counts:
            counts[letter.lower()] += 1
        else:
            counts[letter] = 1 
            order.append(letter)
    while items < len(counts):
        for letter in order:
            if counts[letter] == 1:
                return letter
            elif counts[letter] > 1 :
                items += 1
            elif items == len(counts):
                return " "
            else:
                return " "
    return " "
print(nonRepeatingCharacter(sys.argv[1]))