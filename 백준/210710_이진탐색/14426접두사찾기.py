import sys
N, M = map(int, sys.stdin.readline().split())
m1, m2 = [], []
for i in range(N):
    r1 = sys.stdin.readline()[:-1]
    m1.append(r1)
for i in range(M):
    r2 = sys.stdin.readline()[:-1]
    m2.append(r2)
    
print(m1)
print(m2)
cnt=0
for word in m1:
    for chk_sub_word in m2:
        if word[0]==chk_sub_word[0]:
            for _ in range(len(chk_sub_word)):
                if chk_sub_word[_]!=word[_]:
                    break
            else:
                print(chk_sub_word)
                cnt+=1
print(cnt)