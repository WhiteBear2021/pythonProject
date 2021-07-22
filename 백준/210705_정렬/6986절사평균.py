import sys
def avg(arr):
        length=len(arr)
        sum_vals=0
        for val in arr:
            sum_vals+=val
        return sum_vals/length

# 점수 총 갯수 N, 양쪽에서 수정할 점수 갯수 M
N,M=map(int, sys.stdin.readline().split())


score_arr=[float(sys.stdin.readline()) for _ in range(N)]
score_arr.sort()
# print(N,M,score_arr)

cut_avg_arr=[]
cor_avg_arr=score_arr[0:]
front_cor_val=score_arr[M]
back_cor_val=score_arr[N-M-1]
for i in range(len(score_arr)):
    if i<M:
        cor_avg_arr[i]=front_cor_val
    elif i>=N-M:
        cor_avg_arr[i]=back_cor_val
    else:
        cut_avg_arr.append(score_arr[i])

# print(cut_avg_arr,cor_avg_arr)
print("{:.2f}".format(avg(cut_avg_arr)))
print("{:.2f}".format(avg(cor_avg_arr)))