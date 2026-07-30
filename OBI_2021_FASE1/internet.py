x = int(input())
n = int(input())
acumulado = 0

for i in range(n):
    m = int(input())
    acumulado += x - m

print(acumulado+x)
