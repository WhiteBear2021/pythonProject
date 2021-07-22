import sys
N, M = map(int, sys.stdin.readline().split())
m1, m2 = [], []
for i in range(N):
    r1 = list(map(int, sys.stdin.readline()[:-1]))
    m1.append(r1)
for i in range(N):
    r2 = list(map(int, sys.stdin.readline()[:-1]))
    m2.append(r2)
print(m1)
print(m2)