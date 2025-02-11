t = 0
i,p = 0, 0
while t >= 0:
    t = int(input())
    if t > 0:
        i += t
        p += 1
    else:
        i = i/p
        break
print(f'{i:.2f}')
