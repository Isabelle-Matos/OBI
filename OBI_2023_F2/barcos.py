# ALGORITMO DE ARVORE MAXIMA AINDA NÃO IMPLEMENTADO


# from collections import deque

# def bfs(grafo, inicio):
#     visitados = set()
#     q = {int(v) for v in grafo}
#     # fila = deque([inicio])
#     valores = {}
#     for chave in grafo.keys():
#         if chave not in valores:
#             valores[chave] = 0
#         print(f'chave {chave} e valor {valores[chave]}')

#     q = {int(v) for v in grafo}
#     # chave = {v: int(v) for v in grafo}
#     # print(chave)
#     while q:
#         sub_grafo = grafo[]
#         conjunto = ()
#         vertice = fila.popleft()

#         if vertice not in visitados:
#             print(vertice)
#             sub_grafo = grafo[vertice]
#             chave_maior, valor_maior = max(sub_grafo.items(), key=lambda item: item[1])

      
#             soma.append(valor_maior)

#             visitados.add(vertice)
#             print(f'visitados {visitados}')
#             for chave in sub_grafo.keys():
#                 fila.append(chave)
#             print(soma)
#     return soma
# n, b = [int(x) for x in input().split()]

# grafo={}

# for i in range(b):
#     s1, s2, p = [int(x) for x in input().split()]
#     if s1 not in grafo:
#         grafo[s1] = {}
#     if s2 not in grafo:
#         grafo[s2] = {}
    
#     grafo[s1][s2] = p
#     grafo[s2][s1] = p
    

# soma = []
# soma = bfs(grafo, 2)
# print(min(soma))
