# > 127  = Branco - nao preenchido
# <= 127 = Preto - preenchido

a = True

while a:
    q = int(input())
    if q != 0:
        while q > 0:
            notas = []
            p = list(map(int,input().split()))

            for x in p:
                if x <= 127:
                    notas.append('P')
                else:
                    notas.append('B')
            if notas.count('P') != 1:
                print('*')
            elif notas[0] == 'P':
                print('A')
            elif notas[1] == 'P':
                print('B')
            elif notas[2] == 'P':
                print('C')
            elif notas[3] == 'P':
                print('D')
            elif notas[4] == 'P':
                print('E')

            q -= 1
    else:
        a = False
