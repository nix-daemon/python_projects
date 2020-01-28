#In challenge10.py, write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of 
#those numbers in the form of a phone number.
#Example:
#createPhoneNumber(123456789)
#Output:
#(123) 456-7890
import sys
def createPhoneNumber(array):
    a, b, c, d, e, f, g, h, i, j = array
    # a = array[1]
    # b = array[2]
    # c = array[3]
    # d = array[4]
    # e = array[5]
    # f = array[6]
    # g = array[7]
    # h = array[8]
    # i = array[9]
    # j = array[10]
    print("({}{}{}) {}{}{}-{}{}{}{}".format(a,b,c,d,e,f,g,h,i,j))
createPhoneNumber(sys.argv[1])
