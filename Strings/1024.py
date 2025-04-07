t = int(input())

def troca_reverte(string):
    new = []
    for i in string:
        if i.isalpha():
            i = chr(ord(i)+3)
            new.append(i)
        else:
            new.append(i)
    new.reverse()
    return new

def troca2(string):
    tam = len(string)
    if tam % 2 != 0: #string é impar
        metade = tam // 2
    elif tam % 2 == 0:
        metade = tam // 2
    comeco = string[:metade]
    for i in string[metade:]:
        i = chr(ord(i)-1)
        comeco.append(i)

    print(*comeco, sep='')

while t > 0:
    passw = str(input())
    nova = troca_reverte(passw)
    troca2(nova)
    t -= 1
