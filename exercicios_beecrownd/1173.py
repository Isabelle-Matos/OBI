vetor = []

for i in range(10):
    if i == 0:
        x = int(input())
        aux = x
        vetor.append(x)
        print(aux)
        print('\n')
    else:
        aux = aux * 2
        vetor.append(aux)
        print(aux)
        
for i in range(10):
    print("N[%d] ="%i, vetor[i])

