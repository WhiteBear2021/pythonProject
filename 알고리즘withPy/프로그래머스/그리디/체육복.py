def solution(n, lost, reserve):
    answer = 0
    # idx_list=list(map(lambda index:index-1, idx_list))
    cloth_list=[1]*(n+1)
    for i in lost:
        cloth_list[i]=0
    for j in reserve:
        cloth_list[j]+=1
    cnt=0
    for k in range(1,n+1):
        if cloth_list[k]==0:
            if k==1:
                if cloth_list[k+1]==2:
                    cloth_list[k+1]=1
                    cloth_list[k]=1
                else:
                    cnt+=1
            elif k==n:
                if cloth_list[k-1]==2:
                    cloth_list[k-1]=1
                    cloth_list[k]=1
                else:
                    cnt+=1
            else:
                if cloth_list[k-1]==2:
                    cloth_list[k-1]=1
                    cloth_list[k]=1
                else:
                    if cloth_list[k+1]==2:
                        cloth_list[k+1]=1
                        cloth_list[k]=1
                    else:
                        cnt+=1
    print(cloth_list)
    answer=n-cnt
    return answer

# n	lost	reserve	return
# 5	[2, 4]	[1, 3, 5]	5
# 5	[2, 4]	[3]	4
# 3	[3]	[1]	2

print(solution(5,[2, 4],[1, 3, 5]))