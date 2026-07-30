matriz = []
n = int(input())

for i in range(n):
    linha = [int(valor) for valor in input().split()]
    matriz.append(linha)

valor = n * n
lista = list(range(1, valor+ 1))

for i in range(n):
    for j in range(n):
        if matriz[i][j] == 0:
            linha = i
            coluna = j
            break

for i in range(n):
    for j in range(n):
        if matriz[i][j] in lista:
            indice = lista.index(matriz[i][j])
            lista[indice] = -1

for i in lista:
    if i != -1:
        num = i

print(num)
print(linha+1)
print(coluna+1)

