#Create a program that takes (at least) three command line arguments.  The first two will be integers; the third will
#be a float.
#On one line, separated by spaces, print the sum of the first two arguments, the product of the first and third arguments,
#the first argument modulo the second, and the integer quotient of the third by the first.
#Add 1 to all three arguments.
#On a new line, print the first argument bitwise right shift 3, the second argument divided by 2 (not integer division),
#and the bitwise OR of the first and second arguments.  (all separated by spaces.)
#On the last line, print the sum of the first argument (after the addition) and the total number of arguments,
#excluding the program name.
import sys
def myFunc():
    arg1 = int(sys.argv[1])
    arg2 = int(sys.argv[2])
    arg3 = float(sys.argv[3])
    add = arg1 + arg2
    product = arg1 * arg3
    modulo = arg1 % arg2
    div = arg3 // arg1
    print(add,product,modulo,div)
    arg1 = int(sys.argv[1]) + 1
    arg2 = int(sys.argv[2]) + 1
    arg3 = float(sys.argv[3]) + 1
    print(arg1>>3,arg2/2,arg2|arg1)
    print(arg1+(len(sys.argv)-1))
myFunc()