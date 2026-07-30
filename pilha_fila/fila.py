expressao = input()

x = 0

fila = []

for i in expressao:
    fila.append(i)

tam = len(fila)

while tam > 1:

    if fila[x] != fila[-1]:
        fila.pop(0)
    
    tam -= 1

print("".join(fila))