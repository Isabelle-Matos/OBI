def dfs(grafo, i, visitados):
    p = []
    p.append(i)
    while len(p) != 0:
        v = p[-1]
        p.pop()
        # print(f"topo da pilha {v}")
        for j in grafo[v]:
            if visitados[j] != 1:
                visitados[j] = 1
                p.append(j)

n, m = [int(x) for x in input().split()]
grafo = {}
visitados = [0] * n
count = 0
grafo = {i: [] for i in range(n)}

for i in range(m):
    s1, s2 = [int(x) for x in input().split()]
    s1 -= 1
    s2 -= 1
    if s1 not in grafo:
        grafo[s1] = []
    if s2 not in grafo:
        grafo[s2] = []
    grafo[s1].append(s2)
    grafo[s2].append(s1)

for i in range(n):
    if visitados[i] != 1:
        visitados[i] = 1
        count+=1
        dfs(grafo, i, visitados)

print(count)

# for i, j in grafo.items():
#     print(i, j)
