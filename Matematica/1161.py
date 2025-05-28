t = True
result = []
def fac(numero):
    x = numero
    if numero == 1 or numero == 0:
        x = 1
    else:
        while numero>1:
            x = x*(numero-1)
            numero -= 1
    return x
while t:
    try:
        m,n = list(map(int, input().split()))
        a = fac(m)
        b = fac(n)
        result.append(a+b)
    except EOFError:
        t = False
        print(*result, sep='\n')
    except ValueError:
        t = False
        print(*result, sep='\n')
