def dfs(grafo, x_ini, y_ini):
    if vertice not in visitados:
        print(vertice)
        conjunto = set(grafo[vertice])
        visitados.add(vertice)
        for vizinho in conjunto - visitados:
            dfs(grafo, vizinho, visitados)




n, m = [int(x) for x in input().split()]

grafo = [[0 for i in range(m)] for i in range(n)]

x_ini = 0
y_ini = 0

for i in range(n):
    linha = input().strip()  # Ler uma linha do mapa

    for j in range(m):
        if linha[j] == 'H':  
            grafo[i][j] = 1
        if linha[j] == 'o':
            grafo[i][j] = -1
            x_ini = i
            y_ini = j  
        
    

for i in range(n):
    print(grafo[i])
