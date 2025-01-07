t = int(input())
x = 1
while x <= t:
    heroes = list(map(str, input().split()))
    if heroes[0] != 'Thor':
        print('N')
    else:
        print('Y')
    heroes = []
    x += 1
