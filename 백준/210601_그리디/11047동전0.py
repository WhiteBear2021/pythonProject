def find_coin_cnt(n,k):
    coin_arr=[]
    coin_cnt=0
    # money=k
    for i in range(n):
        coin_arr.append(int(input()))
    for x in range(len(coin_arr)-1,-1,-1):
        each_coin_cnt=k//coin_arr[x]
        coin_cnt+=each_coin_cnt
        k-=(each_coin_cnt*coin_arr[x])
    print(coin_cnt)
        # print(coin_arr[x])
# 리스트 거꾸로 읽는 방법 있나?
n,k=input().split()
find_coin_cnt(int(n),int(k))
