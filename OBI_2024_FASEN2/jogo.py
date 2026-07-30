def bordas_sup_esq(matriz, m, i, j):
    count = 0
    if matriz[i][j+1] == 1:
        count += 1
    if matriz[i+1][j] == 1:
        count += 1
    if matriz[i+1][j+1] == 1:
        count += 1
    if matriz[i][j] == 0 and count == 3:
        m[i][j] = 1
    elif matriz[i][j] == 1 and count == 2 or count == 3:
        m[i][j] = 1
    elif matriz[i][j] == 1 and count < 2:
        m[i][j] = 0
    return m

def bordas_sup_dir(matriz, m, i, j):
    count = 0
    if matriz[i][j-1] == 1:
        count += 1
    if matriz[i+1][j] == 1:
        count += 1
    if matriz[i+1][j-1] == 1:
        count += 1
    if matriz[i][j] == 0 and count == 3:
        m[i][j] = 1
    elif matriz[i][j] == 1 and count == 2 or count == 3:
        m[i][j] = 1
    elif matriz[i][j] == 1 and count < 2:
        m[i][j] = 0
    return m

def bordas_inf_esq(matriz, m, i, j):
    count = 0
    if matriz[i][j+1] == 1:
        count += 1
    if matriz[i-1][j] == 1:
        count += 1
    if matriz[i-1][j+1] == 1:
        count += 1
    if matriz[i][j] == 0 and count == 3:
        m[i][j] = 1
    elif matriz[i][j] == 1 and count == 2 or count == 3:
        m[i][j] = 1
    elif matriz[i][j] == 1 and count < 2:
        m[i][j] = 0
    return m

def bordas_inf_dir(matriz, m, i, j):
    count = 0
    if matriz[i][j-1] == 1:
        count += 1
    if matriz[i-1][j] == 1:
        count += 1
    if matriz[i-1][j-1] == 1:
        count += 1
    if matriz[i][j] == 0 and count == 3:
        m[i][j] = 1
    elif matriz[i][j] == 1 and count == 2 or count == 3:
        m[i][j] = 1
    elif matriz[i][j] == 1 and count < 2:
        m[i][j] = 0
    return m

def lateral_sup(matriz, m, i, j):
    count = 0
    if matriz[i][j-1] == 1:
        count += 1
    if matriz[i][j+1] == 1:
        count += 1
    if matriz[i+1][j-1] == 1:
        count += 1
    if matriz[i+1][j] == 1:
        count += 1
    if matriz[i+1][j+1] == 1:
        count += 1
    if matriz[i][j] == 0 and count == 3:
        m[i][j] = 1
    elif matriz[i][j] == 1 and count == 2 or count == 3:
        m[i][j] = 1
    elif matriz[i][j] == 1 and count < 2:
        m[i][j] = 0
    return m

def lateral_inf(matriz, m, i, j):
    count = 0
    if matriz[i][j-1] == 1:
        count += 1
    if matriz[i][j+1] == 1:
        count += 1
    if matriz[i-1][j-1] == 1:
        count += 1
    if matriz[i-1][j] == 1:
        count += 1
    if matriz[i-1][j+1] == 1:
        count += 1
    if matriz[i][j] == 0 and count == 3:
        m[i][j] = 1
    elif matriz[i][j] == 1 and count == 2 or count == 3:
        m[i][j] = 1
    elif matriz[i][j] == 1 and count < 2:
        m[i][j] = 0
    return m

def lateral_esq(matriz, m, i, j):
    count = 0
    if matriz[i][j+1] == 1:
        count += 1
    if matriz[i-1][j] == 1:
        count += 1
    if matriz[i-1][j+1] == 1:
        count += 1
    if matriz[i+1][j] == 1:
        count += 1
    if matriz[i+1][j+1] == 1:
        count += 1
    if matriz[i][j] == 0 and count == 3:
        m[i][j] = 1
    elif matriz[i][j] == 1 and count == 2 or count == 3:
        m[i][j] = 1
    elif matriz[i][j] == 1 and count < 2:
        m[i][j] = 0
    return m

def lateral_dir(matriz, m, i, j):
    count = 0
    if matriz[i][j-1] == 1:
        count += 1
    if matriz[i+1][j-1] == 1:
        count += 1
    if matriz[i+1][j] == 1:
        count += 1
    if matriz[i-1][j-1] == 1:
        count += 1
    if matriz[i-1][j] == 1:
        count += 1
    if matriz[i][j] == 0 and count == 3:
        m[i][j] = 1
    elif matriz[i][j] == 1 and count == 2 or count == 3:
        m[i][j] = 1
    elif matriz[i][j] == 1 and count < 2:
        m[i][j] = 0
    return m

def centro(matriz, m, i, j):
    count = 0
    if matriz[i][j-1] == 1:
        count += 1
    if matriz[i][j+1] == 1:
        count += 1
    if matriz[i+1][j-1] == 1:
        count += 1
    if matriz[i+1][j] == 1:
        count += 1
    if matriz[i+1][j+1] == 1:
        count += 1
    if matriz[i-1][j-1] == 1:
        count += 1
    if matriz[i-1][j] == 1:
        count += 1
    if matriz[i-1][j+1] == 1:
        count += 1
    if matriz[i][j] == 0 and count == 3:
        m[i][j] = 1
    elif matriz[i][j] == 1 and count == 2 or count == 3:
        m[i][j] = 1
    elif matriz[i][j] == 1 and count < 2:
        m[i][j] = 0
    return m

def zerar_matriz():
    m = [[0 for i in range(n)] for i in range(n)]
    return m

n, k = [int(x) for x in input().split()]

matriz = []
qtd = 0
m = zerar_matriz()
count = 0


for i in range(n):
    linha = input()
    matriz.append([int(x) for x in linha])


while qtd != k:
    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                m = bordas_sup_esq(matriz, m, i, j)

            elif i == 0 and j == n-1:
                m = bordas_sup_dir(matriz, m, i, j)

            elif i == n-1 and j == 0:
                m = bordas_inf_esq(matriz, m, i, j)

            elif i == n-1 and j == n-1:
                m = bordas_inf_dir(matriz, m, i, j)

            elif i == 0 and j != n-1 and j != 0:
                m = lateral_sup(matriz, m, i, j)

            elif i == n-1 and j != n-1 and j!= 0:
                m = lateral_inf(matriz, m, i, j)

            elif j == 0 and i != n-1 and i != 0:
                m = lateral_esq(matriz, m, i, j)

            elif j == n-1 and i != n-1 and i != 0:
                m = lateral_dir(matriz, m, i, j)

            else:
                m = centro(matriz, m, i, j)
                
            count = 0
    matriz = m
    qtd +=1
    m = zerar_matriz()

for i in range(n):
    print("".join(map(str, matriz[i])))