s, t = [int(x) for x in input().split()]
dicionario = {}

for i in range(t):
    s1, s2 = [int(x) for x in input().split()]
    s1 -= 1
    s2 -= 1
    if s1 not in dicionario:
        dicionario[s1] = []
    if s2 not in dicionario:
        dicionario[s2] = []

    dicionario[s1].append(s2)
    dicionario[s2].append(s1)

qtd_seq = 0
sugestoes = int(input())

for i in range(sugestoes):
    lista = [int(x) for x in input().split()]
    tam_seq = lista[0]

    for i in range(2, len(lista)): # 1 0 3
        dir_1 = lista[i] - 1 # 3
        dir_2 = lista[i-1] - 1 # 0
        
        if dir_2 in dicionario.get(dir_1):
            factiveis = 1
        
        else:
            factiveis = 0
            break
    
    if factiveis == 1:
        qtd_seq += 1

print(qtd_seq)

        