#Create a function called factorial that takes one integer argument and calculates its factorial. A factorial is the
#product of a whole number and all the positive whole numbers beneath it.  For example, 4 factorial (usually written 4!)
#is 4x3x2x1 = 24.  The factorial function should print the factorial value.  It should not return a value.
import sys
def factor(n):
    x=1
    if n < 0:
        sys.exit("I'm sorry Dave, I'm afraid I can't do that")
    if n == 1 or n == 0:
        print(1)
    else:
        for i in range(1, n+1):
            x = x * i
        print(x)

if __name__ == "__main__":
    factor(int(sys.argv[1]))
    #factor(-1)