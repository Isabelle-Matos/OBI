from collections import deque

def bfs(grafo, inicio):
    visitados = set()
    fila = deque([inicio])
    while fila:
        conjunto = ()
        vertice = fila.popleft()
        if vertice not in visitados:
            print(vertice)
            conjunto = set(grafo[vertice])
            print(f'conjunto {conjunto}')
            visitados.add(vertice)
            print(f'visitados {visitados}')

            print(f'fila antes {fila}')
            fila.extend(conjunto - visitados)
            print(f'fila depois {fila}')

n, m, x = [int(x) for x in input().split()]
lista =[int(x) for x in input().split()]
grafo = {}

for i in range(m):
    s1, s2 = [int(x) for x in input().split()]
    if s1 not in grafo:
        grafo[s1] = []
    if s2 not in grafo:
        grafo[s2] = []
    grafo[s1].append(s2)
    grafo[s2].append(s1)

bfs(grafo, x)