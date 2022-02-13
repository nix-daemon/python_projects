#for challenge 7,
#Write a function named counts that counts all of the occurring characters in a string (UTF-8).  If you have a string
#like "aba", the result should be {"a":2, "b":1}  If the string is empthy, return {}.
#Example:
#counts("aba")
#Output:
#{"a":2, "b":1}
import sys
test_str = "aba"
all_freq = {}
def count(test_str):
    for i in test_str:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1
    print(all_freq)
count(sys.argv[1])