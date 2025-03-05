i = 1
j = 7
x = 3
while j <= 15:
    while x > 0:
        print(f'I={i} J={j}')
        x -= 1
        j -= 1
    j += 5
    i += 3
    i -= 1
    x = 3
