n = int(input())

m = [[0 for i in range(n)] for i in range(n)]

for i in range(n):
    s1, s2 = [int(x) for x  in input().split()]
    s1 -= 1
    s2 -= 1
    m[s1][s2] = 1
    m[s2][s1] = 1


for i in range(n):
    print(m[i])
