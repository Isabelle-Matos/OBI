def bfs(grafo, origem, destino, pesos):

    fila = []
    
    fila += grafo.get(origem) # [1, 4]

    search = set()

    search.add(vertice)


    while search:
        vertice = fila.pop()

        if pesos[vertice-1] > pesos[origem-1]:
            fila.pop()
        else:
            nova_rota = grafo.get(vertice)
        
            if nova_rota:
                s += nova_rota

        search.add(vertice)
            




s, t, p = [int(x) for x in input().split()]

# 100 150 -50 200

lista_pesos = [int(x) for x in input().split()]

# 1:[2,3], 2:[1,4], 3:[1,4], 4:[2,3,1]

grafo = {}
for i in range(t):
    s1, s2 = [int(x) for x in input().split()]

    if s1 not in grafo:
        grafo[s1] = []
    if s2 not in grafo:
        grafo[s2] = []

    grafo[s1].append(s2)
    grafo[s2].append(s1)


for i, j in grafo.items():
    print(i, j)