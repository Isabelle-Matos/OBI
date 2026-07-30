n = int(input())
dicionario = {}
# string = input()
# lista = []
# count = 1
# for i in string:
#     if i in dicionario:
#         valor = dicionario[i]
#         valor+= 1
#         dicionario[i] = valor
#     else:
#         dicionario[i] = count

for i in range(n):
    u, v = map(int, input().split())
    if u not in dicionario:
        dicionario[u] = []
    if v not in dicionario:
        dicionario[v] = []
    
    dicionario[u].append(v)
    dicionario[v].append(u)

for vertice, vizinhos in dicionario.items():
    print(f'Vertice {vertice}: {vizinhos}')

for valores in dicionario.values():
    print(f'Valores: {valores}')