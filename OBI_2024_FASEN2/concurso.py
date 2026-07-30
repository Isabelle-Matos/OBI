def lista_decr(lista):
    lista_dec = sorted(lista, reverse=True)
    return lista_dec

def criar_lista():
    lista = [int(x) for x in input().split()]
    return lista


n, k = [int(x) for x in input().split()]
lista = criar_lista()
lista_dec = lista_decr(lista)

print(lista_dec[k-1])