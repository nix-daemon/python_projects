#Project 3: Password Checker - Due End of Day 10
#Create a script containing a function demonstrating loops, multiple conditions,
#and return values.
#The function should take one argument, a string containing a password.
#Checks that the input string (password) follows the following guidelines:
#1. Password must be at least 14 characters in length
#2. Password must contain at least one character from each of the following four character sets:
#* Uppercase characters (string.ascii_uppercase)
#* Lowercase characters (string.ascii_lowercase)
#* Numerical Digits (string.digits)
#* Special Characters (string.punctuation)
#3. Password cannot contain more than three consecutive characters from the same character set.
#4. Password cannot contain whitespace characters (string.whitespace)
#5. Returns True if a valid password. False, otherwise.
#Output: True/False
#Examples:
#>>> password_checker("abcABC123!@#abcABC123!@#")
#True
#>>> password_checker("abcdefgABCDEFG1234567!@#$%^&")
#False
#>>> password_checker("abcABC123abcABC123")
#False
#>>> password_checker("aaBB11@@")
#False
#Testing with testpasswords.pyc:
#> python testpasswords.pyc --module password_functions.py --checker password_checker