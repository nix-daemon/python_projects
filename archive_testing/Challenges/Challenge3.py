#For this challenge, you will be given at least three command line arguments.  The first two will be integers;
#the third will be a string.  Use what you have learned so far to create a program which accomplishes the following:
#Prints the larger of the two integers.  If they are equal, do not print either one.
#If the word "time" appears in the string, print the sum of the integers.
#If both the integers are odd, or one of them is a multiple of 3, print the string.
#If there are more than three command line arguments (excluding the filename), print the word "error".
import sys
def Cond():
    arg1 = int(sys.argv[1])
    arg2 = int(sys.argv[2])
    mystring = sys.argv[3]
    word = "time"
    if arg1>arg2:
        print(arg1)
    elif arg1<arg2:
        print(arg2)
    else:
        pass
    if word in mystring:
        print(arg1+arg2)
    else:
        pass
    if arg1 % 2 != 0 and arg2 %2 != 0:
        print(mystring)
    elif arg1 % 3 == 0 or arg2 % 3 == 0:
        print(mystring)
    if len(sys.argv) > 4:
        print("error")
Cond()