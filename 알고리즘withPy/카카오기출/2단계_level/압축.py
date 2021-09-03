def solution(msg):
    answer = []
    hash={}
    for _ in range(1,27):
        hash[chr(_+64)]=_
    print(hash)
    # A~Z넣는법
    # myDic = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", range(1,27)))
    num=26
    n=0
    i=0
    while i<len(msg):
        if hash.get(msg[i]):
            st=""
            for j in range(i,len(msg)):
                st+=msg[j]
                if hash.get(st):
                    val=hash[st]
                    i=j+1
                    if i>=len(msg):
                        answer.append(val)
                else:
                    num+=1
                    hash[st]=num
                    answer.append(val)
                    break
            print(i,j)
    return answer
# print(ord("A"))
# print(ord("Z"))
print(solution("KAKAO"))