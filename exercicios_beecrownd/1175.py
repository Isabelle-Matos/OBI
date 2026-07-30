vetor = []


for i in range(20):
    a = int(input())
    vetor.append(a)
    
for i in range(10):
    aux = vetor[i]
    vetor[i] = vetor[19-i]
    vetor[19-i] = aux

for i in range(20):
    print('N[%d] ='%i,vetor[i])
    

