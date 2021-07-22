n=int(input())
# 도시사이 거리 배열
length_arr=list(map(int, input().split()))
# 도시별 가격 배열
price_arr = list(map(int, input().split()))
# print(n)
# print(length_arr)
# print(price_arr)
min_price=price_arr[0]
sum_price=price_arr[0]*length_arr[0]

for i in range(1,len(length_arr)):
    if  min_price>price_arr[i]:
        min_price=price_arr[i]
    sum_price+=min_price*length_arr[i]
    print(sum_price)
print(sum_price)