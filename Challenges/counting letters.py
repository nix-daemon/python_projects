import collections, sys
f = open("C:\\Users\\170A\\Documents\\GitHub\\170A-Python\\Challenges\\large.txt")
data = f.read()
newdata = data.replace(" ", "")
list = newdata.split()
def filecharcount(openfile):
    return sorted(collections.Counter(c for l in openfile for c in l).items())
print(filecharcount(f))
print(list)