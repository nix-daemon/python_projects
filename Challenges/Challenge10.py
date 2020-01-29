#In challenge10.py, write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of 
#those numbers in the form of a phone number.
#Example:
#createPhoneNumber(123456789)
#Output:
#(123) 456-7890
import sys
def createPhoneNumber(array):
    justNum = array.replace("[", "").replace("]", "")
    newList = justNum.split(",")
    a, b, c, d, e, f, g, h, i, j = newList
    print("({}{}{}) {}{}{}-{}{}{}{}".format(a,b,c,d,e,f,g,h,i,j))
createPhoneNumber(sys.argv[1])