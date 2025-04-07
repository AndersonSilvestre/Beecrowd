c = int(input())
while c > 0:
    n, k = map(int,input().split())
    garrafas = (n%k) + (n//k)
    print(garrafas)
    c -= 1
