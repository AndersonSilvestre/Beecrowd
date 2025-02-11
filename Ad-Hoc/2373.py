t = int(input())
cq = 0
while t > 0:
    l, c = map(int, input().split())
    if l > c:
        cq += c
    else:
        pass
    t -= 1
print(cq)
