import sys

# 도현이 집의 갯수 N, 와이파이 갯수 C
# 5 3
N,C=map(int,sys.stdin.readline().split())

# 도현이의 집 위치 x_list
# 1 2 4 8 9
x_list=sorted([int(sys.stdin.readline().strip()) for _ in range(N)])
print(N,C,x_list)
if C==2:
    print(x_list[-1]-x_list[0])
else:
    cur_max_idx=len(x_list)-1
    cur_min_idx=0
    cur_mid_idx=(cur_max_idx+cur_min_idx)//2
    cur_mid_min_idx=cur_mid_idx
    cur_mid_max_idx=cur_mid_idx
    # 제일 첫과 끝 값
    C-=3
    # 거리 최댓값 num1 if num1 > num2 else num2
    max_distance=x_list[cur_mid_idx]-x_list[cur_min_idx] if x_list[cur_mid_idx]-x_list[cur_min_idx]<x_list[cur_max_idx]-x_list[cur_mid_idx] else x_list[cur_max_idx]-x_list[cur_mid_idx]

    print(cur_max_idx,cur_mid_idx,cur_min_idx,max_distance)
    while C>0:
        min_mid_idx=(cur_mid_min_idx+cur_min_idx)//2
        min_mid_distance=x_list[cur_mid_min_idx]-x_list[min_mid_idx] if x_list[cur_mid_min_idx]-x_list[min_mid_idx]<x_list[min_mid_idx]-x_list[cur_mid_min_idx] else x_list[min_mid_idx]-x_list[cur_mid_min_idx]
        max_mid_idx=(cur_max_idx+cur_mid_max_idx)//2    
        max_mid_distance=x_list[cur_max_idx]-x_list[max_mid_idx] if x_list[cur_max_idx]-x_list[max_mid_idx]<x_list[max_mid_idx]-x_list[cur_mid_max_idx] else x_list[max_mid_idx]-x_list[cur_mid_max_idx]
        if max_mid_distance>min_mid_distance:
           cur_mid_max_idx         