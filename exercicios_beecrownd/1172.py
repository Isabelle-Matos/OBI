
vetor = []

for x in range(10):
    x = int(input())
    if x <= 0:
        x = 1
    vetor.append(x)

for i in range(10):
    print("X[%d] ="%i, vetor[i])
 