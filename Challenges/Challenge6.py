#In this challenge, create two functions:
#which_fibonacci receives a non-negative integer, which may or may not be a Fibonacci number. If it is, then it returns
#its position in the sequence. For example, 2 is the 4th Fibonacci number. If 1 is given as the argument, the function
#should return 2. If the argument is not a Fibonacci number, the function returns 0.
#next_fibonacci received a non-negative integer and returns the next largest Fibonacci number. If the argument is itself
#Fibonacci number, it should return the next Fibonacci number, not the argument itself. If 1 is received, next_fibonacci
#should return 2.

#Python program to check Fibonacci number
import sys
arg1 = int(sys.argv[1])
def fib(n):
    infib = []
    a, b = 1, 0
    for i in range(n+(n + 1)):
        a, b = b, a + b
        infib.append(a)
        if (n) in infib:
            a, b = b, a + b
            infib.append(a)
            break
    return infib

def which_fibonacci(n):
    if n in infib:
        print("Index: {}".format(infib.index(arg1) + 1))
    else:
        print(0)

def next_fibonacci(x):
    if x in infib:
        y=(infib.index(arg1))
        x=(infib[(y+1)])

    elif x not in infib:
        while x not in infib:
            x += 1
    return x

infib = fib(arg1)
which_fibonacci(arg1)
print("Next: {}".format(next_fibonacci(arg1)))