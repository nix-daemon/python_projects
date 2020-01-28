import re
from string import ascii_lowercase as low, ascii_uppercase as up, digits as dig, punctuation as punc
__consec_lower = re.compile("[a-z]{4}")
__consec_upper = re.compile("[A-Z]{4}")
__consec_digits = re.compile("[\\d]{4}")
__consec_punc = re.compile('[^\\dA-Za-z\\s]{4}')

def password_checker(passw):
    badPass = 0
    while True: 
        if (len(passw)<14): 
            badPass = 1
            break
        elif any((True for x in passw if x not in low + up + dig + punc)):
            badpass = 1
            break
        elif not re.search("[a-z]", passw): 
            badPass = 1
            break
        elif not re.search("[A-Z]", passw): 
            badPass = 1
            break
        elif not re.search("[0-9]", passw): 
            badPass = 1
            break
        elif not re.search("[^\\dA-Za-z\\s]", passw): 
            badPass = 1
            break
        elif not (__consec_lower.search(passw)is None) == True:
            badPass = 1
            break
        elif not (__consec_upper.search(passw)is None) == True:
            badPass = 1
            break
        elif not (__consec_digits.search(passw)is None) == True:
            badPass = 1
            break
        elif not (__consec_punc.search(passw)is None) == True:
            badPass = 1
            break
        else: 
            badPass = 0
            return True
    if badPass == 1: 
        return False