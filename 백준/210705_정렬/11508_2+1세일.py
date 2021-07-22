import sys

# 유제품의 갯수 N
N=int(sys.stdin.readline())
# 유제품의 가격들 List로 받기
product_arr=[]
for i in range(N):
    product_arr.append(int(sys.stdin.readline()))
# 오름차순 정렬
product_arr.sort(reverse=True)
# 내야하는 가격
result_price=0
for idx in range(len(product_arr)):
    if idx%3==2:continue
    result_price+=product_arr[idx]
    
# print(product_arr)
print(result_price)
    