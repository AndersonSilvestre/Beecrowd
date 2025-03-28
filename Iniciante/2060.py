int(input())
d, t, q, c = 0, 0, 0, 0
i = list(map(int, input().split()))
for x in i:
    if x % 2 == 0:
        d += 1
    if x % 3 == 0:
        t += 1
    if x % 4 == 0:
        q += 1
    if x % 5 == 0:
        c += 1

print(f'{d} Multiplo(s) de 2')
print(f'{t} Multiplo(s) de 3')
print(f'{q} Multiplo(s) de 4')
print(f'{c} Multiplo(s) de 5')
