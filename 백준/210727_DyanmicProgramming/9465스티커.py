import sys
read=sys.stdin.readline

# TEST 케이스 횟수
T=int(read())
# TEST 횟수 만큼 반복문으로 실행 해주기
for t in range(T):
    # 2xN 배열에서 N 값 받기
    N=int(read())
    # 띄어쓰기로 2차원 배열 받을 거
    arr=[list(map(int,read().split())) for _ in range(2)]
    if N>1:
        arr[1][1]+=arr[0][0]
        arr[0][1]+=arr[1][0]
        for i in range(2,N):
            arr[1][i]+=max(arr[0][i-2],arr[0][i-1])
            arr[0][i]+=max(arr[1][i-2],arr[1][i-1])
            
    result=max(arr[1][N-1],arr[0][N-1])
    print(result)
    
T = int(input())

for test_case in range(T):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(2)]

    arr[0][1] = arr[0][1] + arr[1][0]
    arr[1][1] = arr[1][1] + arr[0][0]

    for k in range(2, N):
        arr[0][k] = arr[0][k] + max(arr[1][k - 1], arr[1][k - 2])
        arr[1][k] = arr[1][k] + max(arr[0][k - 1], arr[0][k - 2])

    answer = max(arr[0][N-1], arr[1][N-1])
    print(answer)
