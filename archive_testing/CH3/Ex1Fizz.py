# Fizzbuzz: Write a function that prints out the numbers from 1 to 100, except that multiples of 3 are replaced by "fizz"
# and multiples of 5 are replaced by "buzz". Multiples of 3 and 5 should be replaced by "fizzbuzz".
def Fizzbuzz():
	for num in range(1, 101):
		if (num % 3 == 0) and (num % 5 == 0):
			print("Fizzbuzz")
		elif (num % 3 == 0):
		    print("Fizz")
		elif (num % 5 == 0):
		    print("Buzz")
		else:
			print(num)
Fizzbuzz()