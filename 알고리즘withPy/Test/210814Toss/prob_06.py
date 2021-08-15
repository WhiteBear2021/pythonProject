# 6번문제
# https://midason.tistory.com/129

def solution(numOfStairs):
    d=[0]*(numOfStairs+1)
    d[1]=1
    d[2]=2
    d[3]=4
    d[4]=7
    for i in range(5,numOfStairs+1):
        d[i]=d[i-1]+d[i-2]+d[i-3]
    answer = d[numOfStairs]
    return answer

