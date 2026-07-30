n = int(input())
p = [int(i) for i in input().split()]

dist = 0
k = -1

for i in range(n):
    dist_ini = p[0] + i + p[i]

    if dist_ini > dist:
        dist = dist_ini
        k = i

# print(k)
max_d = 0
dist_final = 0

for i in range(n):
    if k > i:
        dist_final = p[i] + p[k] + (k-i)
    else:
        dist_final = p[i] + p[k] + (i-k)

    if dist_final > max_d:
        max_d = dist_final

print(max_d)
