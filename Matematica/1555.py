#Rafael = r(x, y) = (3x)² + y².
#Beto = b(x, y) = 2(x²) + (5y)².
#Carlos = c(x, y) = -100x + y³.

t = int(input())

while t > 0:
    x, y = map(int,input().split())
    r = ((3*x)**2) + y**2
    b = (2*(x**2)) + ((5*y)**2)
    c = (-100*x) + (y**3)
    if r > max(b,c):
        print('Rafael Ganhou')
    elif b > max(c,r):
        print('Beto Ganhou')
    else:
        print('Carlos Ganhou')
    
    t -= 1
