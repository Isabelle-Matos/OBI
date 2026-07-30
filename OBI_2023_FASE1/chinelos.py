
n = int(input())
estoque = []

for i in range(n):
    x = int(input())
    estoque.append(x)

p = int(input())

total = 0
for k in range(p):
    i = int(input())
    if estoque[i-1] > 0:
        estoque[i-1] -= 1
        total += 1

print(total)