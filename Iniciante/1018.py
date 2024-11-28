x = int(input())

print(x)
nota100 = x // 100
z = x%100
print(f'{nota100:.0f} nota(s) de R$ 100,00')
nota50 = z//50
z = z%50
print(f'{nota50:.0f} nota(s) de R$ 50,00')
nota20 = z//20
z = z%20
print(f'{nota20:.0f} nota(s) de R$ 20,00')
nota10 = z//10
z = z%10
print(f'{nota10:.0f} nota(s) de R$ 10,00')
nota5 = z//5
z = z%5
print(f'{nota5:.0f} nota(s) de R$ 5,00')
nota2 = z//2
z = z%2
print(f'{nota2:.0f} nota(s) de R$ 2,00')
nota1 = z//1
z = z%1
print(f'{nota1:.0f} nota(s) de R$ 1,00')