def dfs(grafo, vertice, visitados):
    if vertice not in visitados:
        print(vertice)
        conjunto = set(grafo[vertice])
        visitados.add(vertice)
        for vizinho in conjunto - visitados:
            dfs(grafo, vizinho, visitados)


n, m, x = [int(x) for x in input().split()]
lista =[int(x) for x in input().split()]
grafo = {}
visitados = set()

for i in range(m):
    s1, s2 = [int(x) for x in input().split()]
    if s1 not in grafo:
        grafo[s1] = []
    if s2 not in grafo:
        grafo[s2] = []
    grafo[s1].append(s2)
    grafo[s2].append(s1)

dfs(grafo, x, visitados)