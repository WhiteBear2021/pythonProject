import sys
# 집과 사무실 쌍 갯수 N
N=int(sys.stdin.readline())
# 집과 사무실 위치값 이차원 배열로
loc_arr=[]
for i in range(N):
    loc=list(map(int, sys.stdin.readline().split()))
    loc.sort()
    loc_arr.append(loc)

loc_arr.sort(key=lambda x:x[1])
# 철로 길이 d
d=int(sys.stdin.readline())
max_cnt=0
for i in range(len(loc_arr)-1,-1,-1):
    end_rail=loc_arr[i][1]
    start_rail=end_rail-d
    cnt=0
    for j in range(i,-1,-1):
        # print(f"cnt값 {cnt}")
        if loc_arr[j][0]>=start_rail and loc_arr[j][1]<=end_rail:
            cnt+=1
            # print(start_rail,end_rail)
            # print(i,j,cnt)
        elif loc_arr[j][1]<start_rail:break
    loc_arr.pop()
    # print(loc_arr)
    if cnt>=max_cnt:
        max_cnt=cnt

# print(N,loc_arr,d)
print(max_cnt)