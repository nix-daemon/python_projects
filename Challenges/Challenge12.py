#In challenge12.py, create a class called Number, which is initialized with a positive integer n as its sole argument. 
#It should have at least four methods:
#is_prime returns True if n is prime, and False if not. 1 is not prime.
#get_divisors returns a list of positive divisors of n, in ascending order.
#get_gcd takes a positive integer argument, and
#returns the greatest common divisor of n and the argument.
#get_lcm takes a positive integer argument, and returns the least common (positive) multiple of n and the argument.
import math
import sys
class Number:
    def __init__(self,num):
        self.num = num

    def is_prime(self):
        if self.num > 1:
            for i in range(2,self.num):
                if (self.num % i) == 0:
                    return False
                    break
                else:
                    return True
        else:
            return False

    def get_divisor(self):
        div=[]
        for i in range(1, self.num + 1):
            if self.num % i == 0:
                div.append(i)
        return div

    def get_lcm(self,x):
        a = numIn.get_gcd(x)
        return int((x * self.num) / a)

    def get_gcd(self,x):
        if self.num > x:
            small = x
        else:
            small = self.num
        for i in range(1, small + 1):
            if((self.num % i == 0) and (x % i == 0)):
                gcd = i
        return gcd

numIn=Number(int(sys.argv[1]))
x=int(sys.argv[2])
print("Prime?",numIn.is_prime())
print("Factors:",numIn.get_divisor())
print("GCD n and m:",numIn.get_gcd(x))
print("LCM n and m:",numIn.get_lcm(x))