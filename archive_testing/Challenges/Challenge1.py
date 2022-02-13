#Write a program that:
#Takes the first two command line arguments (excluding the filename).  Both of them will be strings, and both of them will be long enough that you will not get index errors.
#Print those two arguments, separated by a space.
#Prints a string consisting of the first character of the first argument, followed by the third character of the second argument, followed by the last character of the second argument, followed by the length of the first argument.
#Prints two empty lines.
#Prints the total number of arguments (including file name).
#Print the 2nd - 4th characters of the first argument.
#Prints the phrase "use of 'quotation' marks".
#Takes input from the user with the prompt "please enter: " and prints the second character of the user input.
import sys
def myFunc():
    arg1 = str(sys.argv[1])
    arg2 = str(sys.argv[2])
    str1 = arg1[0] + arg2[2] + arg2[-1] + str(len(arg1))
    print(arg1 + " " + arg2)
    print(str1)
    print()
    print()
    print(len(sys.argv))
    print(arg1[1:4])
    print("use of 'quotation' marks")
    userInput = input("please enter:")
    print(userInput[1])
myFunc()