vetor = []


for i in range(10):
    a = float(input())
    vetor.append(a)
    
for i in range(10):
    if vetor[i] <=10.0:
        #print(f'A[%d] = {vetor[i]:.1f}'%i)
        print(f'A[{i}] = {vetor[i]:.1f}')
    

