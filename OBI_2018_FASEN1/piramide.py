N = int(input())

# Criar duas matrizes nulas
m = [[0 for i in range(N+1)] for i in range(N+1)]
dp = [[0 for i in range(N+1)] for i in range(N+1)]

# Lê a entrada e armazena dentro da matriz
for i in range(1, N+1):
    linha = [int(x) for x in input().split()]
    for j in range(1, N+1):
        m[i][j] = linha[j-1]


for i in range(1, N+1):
    print(f"Interacao", {i})
    for j in range(i, N+1):
        print(f"valor do j", {j})
        for k in range(j, j-i, -1):
            print("valor do i j e k:", i, j, k)
            dp[i][j] += m[i][k]
            print(dp[i][j])
        if i > 1:
            dp[i][j] += min(dp[i-1][j], dp[i-1][j-1])
            print(dp[i][j])
    
print(dp[N][N])