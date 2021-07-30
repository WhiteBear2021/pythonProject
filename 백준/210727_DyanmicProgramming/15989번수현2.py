t = int(input())
dp = [1 for i in range(10001)]
dp[2] = 2
dp[3] = 3
for i in range(4,10001):
        dp[i] = dp[i - 1] + (dp[i - 2] - dp[i - 3])
        if i%3==0:
            dp[i] = dp[i]+1
for _ in range(t):
    n = int(input())

    print(dp[n])