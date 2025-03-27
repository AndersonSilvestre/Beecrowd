t = int(input())
sub = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'S', 's']
final = []
while t > 0:
    total = 1
    s = input()
    for x in s:
        if x in sub:
            total *= 3
        elif x == ' ':
            continue
        else:
            total *= 2
    final.append(total)
    t -= 1
for y in final:
    print(y)