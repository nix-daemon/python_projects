def myfunc():
    s = 'abcdefghijklmnopqrstuvwxyz'
    s = list(s)
    print("d is at " + str(s.index("d")))
    s[3] = "!"
    print("y is at " + str(s.index("y")))
    s.insert(24, "?")
    print("byebye b")
    s.remove("b")
    s = "".join(s)
    print(s)
myfunc()