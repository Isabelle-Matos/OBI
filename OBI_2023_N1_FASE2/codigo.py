n = int(input())
string = input()
anterior = ''
aux = []
count = 1

for i in string:
    
    if i == anterior:
        count += 1
    else:
        if anterior != '':
            aux.append(f'{count} {anterior}')
            print(aux)
        anterior = i
        # print("valor dentro do else ", anterior)
        count = 1

aux.append(f'{count} {anterior}')
resposta = " ".join(aux)
print(resposta)


## ----------- Utilizando dicionários considerando que o problema deseja saber a quantidade total de valores na string ------------

# TAAAAxxx

# n = int(input())
# dicionario = {}
# string = input() # TAAAAxxx
# count = 1

# for i in string:
#     if i in dicionario:                 # dicionario ={'T': 1, 'A': 4, 'x': 3}
#         valor = dicionario[i]
#         valor+= 1
#         dicionario[i] = valor
#     else:
#         dicionario[i] = count


# XYXY
# print(dicionario)
# 1 T 4 A 
# Acessando as chaves no nosso dicionário
# for i in dicionario:
#     print({i})

# palavra = ''
# # Acessando as chaves e valores no nosso dicionário
# for chave, valor in dicionario.items():
#     aux = f'{valor} {chave} '
#     palavra += aux
    # print(f'Chave: {chave} Valor: {valor}')

# print(len(palavra))
# # print(palavra[-1])
# palavra = palavra[:-1]
# print(len(palavra))
# Acessando valores no dicionário
# for valor in dicionario.values():
#     print(f'Valor: {valor}')

# # Acessando chaves no dicionario
# for chaves in dicionario.keys():
    # print(f'Chave: {chaves}')



