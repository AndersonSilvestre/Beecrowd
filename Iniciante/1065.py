x = 5
z = 0
while x > 0:
    y = int(input())
    if y %2 == 0:
        z += 1
    x -= 1
print(f'{z} valores pares')
