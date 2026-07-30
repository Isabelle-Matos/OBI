n = int(input())

m = [[0 for i in range(n)] for i in range(n)]

for k in range(n):
    for i in range(k, n-k):
        for j in range(k, n-k):
            m[i][j] +=1


for i in range(n):
    for j in range(n-1):
        print(m[i][j], end= ' ') # por padrão o end é /n, podemos mudar colocando end = ' '
    print(m[i][n-1]) # imprime a ultima coluna para cada linha, aqui ele imprime e pula para a proxima linha
