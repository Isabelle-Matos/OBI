n = int(input())
total = 0
atual = 0

for i in range(n):
    num = int(input())

    if  num != atual:
        total +=1
        atual = num

print(total)