n = int(input())
m = int(input())

conjunto = set()

for i in range(m):
    fig = int(input())
    conjunto.add(fig)

tam = len(conjunto)
print(abs(n-tam))