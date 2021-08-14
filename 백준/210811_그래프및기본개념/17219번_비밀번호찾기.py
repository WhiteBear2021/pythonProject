import sys
input=sys.stdin.readline

# 비밀번호가 저장된 사이트 갯수 N, 찾고싶은 비밀번호의 사이트 갯수 M
N,M=map(int,input().split())
# 비밀번호를 저장할 디셔너리 자료구조
dic={}
for _ in range(N):
    # 사이트 주소 a, 비밀번호 p
    a,p=input().split()
    dic[a]=p
  
# print(dic)  
# print(dic['noj.am'])
for _ in range(M):
    answer_p=dic[input()[:-1]]
    print(answer_p)