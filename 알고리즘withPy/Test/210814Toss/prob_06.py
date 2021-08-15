# 6번문제


def solution(numOfStairs):
    d=[0]*71
    d[1]=1
    d[2]=2
    d[3]=4
    d[4]=7
    for i in range(5,71):
        d[i]=d[i-1]+d[i-2]+d[i-3]
        if i%6==0:
            d[i]+=1

    answer = d[numOfStairs]
    return answer