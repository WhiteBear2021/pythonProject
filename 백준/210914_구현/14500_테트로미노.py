# 5 5
# 1 2 3 4 5
# 5 4 3 2 1
# 2 3 4 5 6
# 6 5 4 3 2
# 1 2 1 2 1

# 세로 n 가로 m
n,m=map(int,input().split())

arr=[list(map(int,input().split())) for _ in range(n)]

# 길쭉
def tetno1(i,j,arr):
    sum=0
    if j+3<len(arr[i]):
        for k in range(4):
            sum+=arr[i][j+k]
    return sum
# 네모
def tetno2(i,j,arr):
    sum=0
    if i+1>=len(arr) or j+1>=len(arr[i+1]):
        return sum
    else:
        sum+=arr[i][j]+arr[i][j+1]+arr[i+1][j]+arr[i+1][j+1]
        return sum
# ㄴ 모양
def tetno3(i,j,arr):
    sum=0
    if i+2>=len(arr) or j+1>=len(arr[i+2]):
        return sum
    else:
        sum+=arr[i][j]+arr[i+1][j]+arr[i+2][j]+arr[i+2][j+1]
        return sum
# ㄹ 옆으로
def tetno4(i,j,arr):
    sum=0
    if i+2>=len(arr) or j+1>=len(arr[i+2]):
        return sum
    else:
        sum+=arr[i][j]+arr[i+1][j]+arr[i+1][j+1]+arr[i+2][j+1]
        return sum
# ㅗ 뒤집은
def tetno5(i,j,arr):
    sum=0
    if i+1>=len(arr) or j+2>=len(arr[i]):
        return sum
    else:
        sum+=arr[i][j]+arr[i][j+1]+arr[i+1][j+1]+arr[i][j+2]
        return sum
answer=0        
for i in range(len(arr)):
    for j in range(len(arr[i])):
        answer=max(answer,tetno1(i,j,arr),tetno2(i,j,arr),tetno3(i,j,arr),tetno4(i,j,arr),tetno5(i,j,arr))
        
print(answer)