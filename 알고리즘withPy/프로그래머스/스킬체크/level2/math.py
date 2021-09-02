def solution(n):
    answer = 0
    for i in range(1,n+1):
        sum=0
        for j in range(i,n+1):
            sum+=j
            if sum==n:
                answer+=1
                break
            elif sum>n:
                break
    return answer


# print(solution(15))

# 반례잇음
def solution3(n):
    answer = 0
    i=1
    while True:
        print(i,answer)
        sum=0
        for num in range(i,n+1):
            sum+=num
            if sum==n:
                answer+=1
                i=num+1
                break
            elif sum>n:
                i+=1
                break
        if i>n:
            break
    return answer

print(solution3(15))