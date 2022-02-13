def myfunc():
    s = 'abcdefghijklmnopqrstuvwxyz'
    li = list(s)
    for i in range(len(li)):
        if li[i] == 'd':
            li.insert(i, '!')
        else:
            continue
        print(li)
myfunc()