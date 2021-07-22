import sys
# 그림 갯수 N, 특정 정수(이 길이 이상이어야 판매가능) S
N,S=map(int, input().split())

height_price_arr=[list(map(int, input().split())) for _ in range(N)]
# height_price_arr = [list(map(int, list(input()))) for _ in range(N)]
height_price_arr.sort(key=lambda x:(x[0],-x[1]))

print(height_price_arr)
price_arr=[]
cur_height=height_price_arr[0][0]
compare_height=cur_height+S
price_arr.append(height_price_arr[0][1])


for i in range(len(height_price_arr)):
    if i==0:continue
    print(cur_height,compare_height)
    if cur_height<=height_price_arr[i][0]<compare_height:
        if height_price_arr[i][1]>price_arr[-1]:
            price_arr[-1]=height_price_arr[i][1]
            cur_height=height_price_arr[i][0]
            compare_height=cur_height+S
    else:
        price_arr.append(height_price_arr[i][1])
        cur_height=height_price_arr[i][0]
        compare_height=cur_height+S
        
print(price_arr)