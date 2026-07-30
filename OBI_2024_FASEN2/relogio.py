h = int(input())
m = int(input())
s = int(input())
t = int(input())

def operacoes(h, m, s, t):
    s += t
    m += s // 60
    s %= 60
    h += m // 60
    m %= 60
    h %= 24

    lista = [h, m, s]

    # retorna uma tupla
    # return h, m, s
    return lista

lista = operacoes(h, m, s, t)
# print(lista)
for i in lista:
    print(i)
