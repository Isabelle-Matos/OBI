# Faça um programa que leia uma expressão com parênteses. Usando pilhas, verifique se os parênteses 
# foram abertos e fechados na ordem correta.


expressao = input()

x = 0

pilha = []

while x < len(expressao):

    if expressao[x] == "(":
        pilha.append("(") # O(1)
    if expressao[x] == ")":
        if len(pilha) > 0:
            pilha.pop(-1) # O(1)
        else:
            break

    x = x + 1

if len(pilha) == 0:
    print("OK")
else:
    print("Erro")