n, k = map(int, input().split())
backpack = []
for _ in range(n):
    backpack.append(list(map(int, input().split())))
dp = [[0 for _ in range(k+1)] for _ in range(n)]
for j in range(0, n):
    w, v = backpack[j]
    for i in range(1, k + 1):
        if w<=i:
            dp[j][i]= max(dp[j-1][i], dp[j-1][i-w]+v)
        else:
            dp[j][i]=dp[j-1][i]
max_n=0
for k in range(n):
    print(dp[k])
    tmp = int(max(dp[k]))
    max_n = max(max_n, tmp)

print(max_n)


