#Project 2: Password Generator - Due End of Day 10
#Create a script containing a function to demonstrating string creation and calling
#a function from another function.
#The function should have one optional argument for length. The default length is 14.
#Generate a password (of given length if provided) that meets the password requirements from Project 1.
#Output: a valid password string
#Example:
#>>> password_generator(length = 24)
#"abcABC123!@#abcABC123!@#"
#>>> password_generator()
#"BANana4!anaNAB"
#Testing with testpasswords.pyc:
#> python testpasswords.pyc --module password_functions.py --generator password_generator
import string
from random import *
def password_generator(length):
    characters = string.ascii_uppercase + string.ascii_lowercase  + string.digits + string.punctuation
    password =  "".join(choice(characters) for x in range(randint(8, 16)))
    print(password)
password_generator(14)