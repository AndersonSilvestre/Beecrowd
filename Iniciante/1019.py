x = int(input())
hrs =x//3600
y = x%3600
minutos = y//60
segundos = y%60

print(f'{hrs}:{minutos}:{segundos}')