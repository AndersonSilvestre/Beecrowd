while True:
    try:
        a,b = map(int, input().split())
        t = a+b
        r = []
        if t != 0:
            for i in str(t):
                if i != '0':
                    r.append(i)
            print(*r,sep='')
        else:
            break
    except EOFError:
        break
