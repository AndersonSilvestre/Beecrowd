v = 2
y = 0
while v > 0:
    n = float(input())
    if n >= 0 and n <= 10:
        y += n
        v -= 1
    else:
        print('nota invalida')
print(f'media = {y/2}')
