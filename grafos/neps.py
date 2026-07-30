def dfs(grafo, vertice, visitados, nao_visitados):
   
    visitados[vertice] = 1

    for vizinho, aresta in enumerate(grafo[vertice]):
        # print(vizinho, aresta)
        if aresta == 0 and vizinho != vertice:
            nao_visitados[vertice] += 1
        if aresta == 1 and not visitados[vizinho]:
            dfs(grafo, vizinho, visitados, nao_visitados)


n, r = [int(x) for x in input().split()]

m = [[0 for i in range(n)] for i in range(n)]

for i in range(r):
    x, y = [int(x) for x in input().split()]
    x -= 1
    y -= 1
    m[x][y] = 1
    m[y][x] = 1

visitados = [0 for i in range(n)]
nao_visitados = [0 for i in range(n)]
dfs(m, 0, visitados, nao_visitados)
if sum(nao_visitados) == 0:
    qtd = 0
else:
    qtd = sum(nao_visitados)//2

print(qtd)
