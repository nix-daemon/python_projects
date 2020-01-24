#This challenge is intended to test your knowledge of loops and previous material.
#Create a program that takes one command line argument.  It will be an integer.
#For each number between 1 and the argument (inclusive), print the word "triangle" if the number is a multiple of three.
#Print "square" if it is a multiple of four.
#If it is a multiple of 12, do not print triangle or square.  Instead, print "x dozen" where x is the numeral representing
#how many dozen you're at("1 dozen" for 12, "2 dozen" for 24, etc.)
#Lastly, print the sum of the numbers between 1 and the argument (inclusive).
def loop(num):
num_list = range(1, num + 1)
final_sum = sum(num_list)
     for i in range(1, (num+1)):
         if i % 12 == 0:
             print("{} dozen".format(i/12))
         elif i % 3 == 0:
             print("triangle")
         elif i % 4 == 0:
             print("square")
      print(final_sum)
