
def dfs(x, y, vigiada, visitada, n, m):

    visitada[x][y] = True

    if x > 1 and not visitada[x-1][y] and not vigiada[x-1][y]:
        dfs(x-1, y, vigiada, visitada, n, m)

    if x < n and not visitada[x+1][y] and not vigiada[x+1][y]:
        dfs(x+1, y, vigiada, visitada, n, m)

    if y > 1 and not visitada[x][y-1] and not vigiada[x][y-1]:
        dfs(x, y-1, vigiada, visitada, n, m)

    if y < m and not visitada[x][y+1] and not vigiada[x][y+1]:
        dfs(x, y+1, vigiada, visitada, n, m)


m, n, k = map(int, input().split())

vigiada = [[False for i in range(m + 1)] for i in range(n + 1)]
visitada = [[False for i in range(m + 1)] for i in range(n + 1)]

for i in range(k):
    camera_info = input().split()
    y = int(camera_info[0])
    x = int(camera_info[1])

    if camera_info[2] == 'N':
        for j in range(1, x + 1):
            vigiada[j][y] = True

    if camera_info[2] == 'S':
        for j in range(x, n + 1):
            vigiada[j][y] = True

    if camera_info[2] == 'O':
        for j in range(1, y + 1):
            vigiada[x][j] = True

    if camera_info[2] == 'L':
        for j in range(y, m + 1):
            vigiada[x][j] = True


dfs(1, 1, vigiada, visitada, n, m)

if vigiada[1][1]:
    print("N")
elif visitada[n][m]:
    print("S")
else:
    print("N")

