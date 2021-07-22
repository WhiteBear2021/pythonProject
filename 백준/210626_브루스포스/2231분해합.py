import sys

target_num=int(sys.stdin.readline())
# 문자열 길이(10의 제곱 구하기 위해 -1)
num_length=len(str(target_num))-1

num_arr=[]
for i in range(num_length,-1,-1):
    num=target_num//(10**i)
    num_arr.append(num)
    target_num-=num*(10**i)

num_arr.sort()

