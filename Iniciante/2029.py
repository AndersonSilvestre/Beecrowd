def volume(v,r):
    r = r/2
    a = 3.14 * (r*r)
    h = v / a
    return a, h
while True:
    try:
        # formula area A = 3.14*r²
        # formula altura H = V / 3.14*r²
        v = float(input())
        d = float(input())
        are, alt = volume(v,d)
        print(f'ALTURA = {alt:.2f}')
        print(f'AREA = {are:.2f}')
    except EOFError:
        break
