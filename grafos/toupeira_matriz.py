s, t = [int(x) for x in input().split()]
m = [[0 for i in range(s)] for i in range(s)]

for i in range(t):
    # lista = [char for char in input().split()]
    s1, s2 = [int(x) for x in input().split()]
    s1 -= 1
    s2 -= 1
    m[s1][s2] = 1
    m[s2][s1] = 1

qtd_seq = 0
sugestoes = int(input())

for i in range(sugestoes):
    lista = [int(x) for x in input().split()]
    tam_seq = lista[0]


    for i in range(2, len(lista)):
        dir_1 = lista[i] - 1
        dir_2 = lista[i-1] - 1

        if m[dir_1][dir_2] == 1:
            factiveis = 1
        else:
            factiveis = 0
            break
        
    if factiveis == 1:
        qtd_seq += 1

print(qtd_seq)
