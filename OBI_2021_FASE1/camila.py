A = input()
B = input()
C = input()

lista = [A, B, C]
lista_ord = []
# Odenação de vetores

lista_ord = sorted(lista)
print(lista_ord[1])

lista.sort()
print(lista[1])

# for i in range(len(lista)):
#     for j in range(i, len(lista)):
#         if lista[i] > lista[j]:
#             aux = lista[i]
#             lista[i] = lista[j]
#             lista[j] = aux

# print(lista[1])