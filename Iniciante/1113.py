a = True
while a:
    a, b = map(int, input().split())
    if a == b:
        a = False
    elif a > b:
        print('Decrescente')
    else:
        print('Crescente')
