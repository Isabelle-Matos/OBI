B = int(input())
T = int(input())

area_metade = (70*160)/2
h = 70
maior = max(B,T)
menor = min(B,T)
base_triangulo = maior- menor
area_triangulo = (base_triangulo*h)/2

if maior == B:
    area_quadrado = T*h
else:
    area_quadrado = B*h


f = area_triangulo + area_quadrado

if f > area_metade:
    print(1)
elif f < area_metade:
    print(2)
else:
    print(0)
