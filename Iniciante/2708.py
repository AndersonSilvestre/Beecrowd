foi = 0
jipes = 0
y =0
ato, pessoa = [], []
while True:
    try:
        a,b = input().split()
        ato.append(a)
        pessoa.append(int(b))
    except ValueError:
        for x in ato:
            if x == 'SALIDA':
                foi += pessoa[y]
                jipes += 1
            else:
                foi -= pessoa[y]
                jipes -= 1
            y +=1
        print(foi)
        print(jipes)
        break
