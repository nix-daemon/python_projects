#In challenge8.py, write a program that does the following:
#Reads in a filename from the command line
#Determines the most common letter in the file, and prints what it is and how many times it occurs. Use the format “_ is
#the most common letter. It occurs _ times.” Replace _ with the appropriate letter (uppercase) and number.
#Determines what percentage of the number of words in the file is the word “the”; print the integer that is closest to
#this percentage, rounding down. Ignore capitalization: “The” and “the” are the same word.
#Writes the first ten words of the file (as determined by whitespace) to a new file named "challenge9_output.txt”.
#Assume the file will be written to the same directory where the challenge9.py file is located.
from collections import Counter
import sys
def readFunc(arg1):
    with open(arg1) as f:
        data = f.read()
        letters = Counter(data.replace(" ", "").upper()).most_common()
        x = letters[0]
        words = data.split()
        totalNumOfWords = len(words)
        totalOccur = Counter(words)
        the_occur = totalOccur.most_common(1)
        thePercent = round((the_occur[0][1] / totalNumOfWords) * 100)
        print("{} is the most common letter. It occurs {} times.".format(x[0], x[1]))
        print("The word 'The' is {}% of the words.".format(thePercent))
        newFile = open("challenge8_output.txt", "w")
        newFile.write(" ".join(map(str, words[0:10])))
readFunc(sys.argv[1])