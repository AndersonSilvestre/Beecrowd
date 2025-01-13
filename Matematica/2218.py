#Ln = (N*(N+1)/2) + 2
#Onde n = retas dadas

t = int(input())
while t > 0:
    n = int(input())
    gap = (n*(n+1)/2) + 1
    print(int(gap))
    t -= 1
