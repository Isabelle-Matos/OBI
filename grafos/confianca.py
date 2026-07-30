from collections import deque


n, m = [int(x) for x in input().split()]
grafo = {i: [] for i in range(n)}
visitados = set()
count = 0

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
    c = set(grafo[i])
    vertice = i
    visitados.add(i)

    while len(c) != n - 1:
        for j in range(n):
            if j not in visitados and j not in c:
                grafo[vertice].append(j)
                grafo[j].append(vertice)
                count+=1
                c.add(j)
    
print(count)