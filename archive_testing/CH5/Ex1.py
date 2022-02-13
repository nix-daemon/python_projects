with open('important.txt') as f:
    for line in f:
        (key) = line.split()
        print(key)