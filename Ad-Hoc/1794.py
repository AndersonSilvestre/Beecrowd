n = int(input())
la, lb = map(int,input().split())
sa, sb = map(int,input().split())

if n >= la and n <= lb:
    if n >= sa and n <= sb:
        print('possivel')
    else:
        print('impossivel')
else:
    print('impossivel')
