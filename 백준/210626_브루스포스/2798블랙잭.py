import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())

m=list(map(int, sys.stdin.readline().split()))
m.sort()
new_m=list(combinations(m,3))
ans=sum(new_m[0])
for i in new_m:
    s=sum(i)
    if s==M:
        ans=s
        break
    if s>ans and s<M:
        ans=s
    
print(ans)