A, B, C = input().split()
A, B, C = int(A), int(B), int(C)

maiorAB = ((A+B)+abs(A-B))/2
maior = ((C+maiorAB)+abs(C-maiorAB))/2
print(f'{maior:.0f} eh o maior')