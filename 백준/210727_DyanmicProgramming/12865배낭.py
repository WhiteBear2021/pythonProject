import sys
read=sys.stdin.readline

# 배낭의 갯수 : N, 담을 수 있는 배낭의 무게 : K
N,K=map(int,read().split())

# 값 저장할 dp 배열
dp=[0 for _ in range(K+1)]

# 배낭의 무게랑 가치 배열로 받기
bags=[list(map(int, list(read().split()))) for _ in range(N)]



for idx in range(len(bags)):
    for k in range(1,K+1):
        if dp[k]==0:
            dp[k]=dp[k-1]
        if k>=bags[idx][0]:
            dp[k]=max(dp[k-1],bags[idx][1]+dp[k-bags[idx][0]])


print(dp[K])