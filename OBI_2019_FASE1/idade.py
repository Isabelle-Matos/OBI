idade_m = int(input())
idade_f1 = int(input())
idade_f2 = int(input())

idade_f3 = idade_m - (idade_f1+idade_f2)

vetor = list()
vetor.append(idade_f1)
vetor.append(idade_f2)
vetor.append(idade_f3)

vetor.sort()
print(vetor[2])

# for i in range(3):
#     for j in range(i,3):
#         if vetor[i] > vetor[j]:
#             aux = vetor[i]
#             vetor[i] = vetor[j]
#             vetor[j] = aux

# print(vetor[2])