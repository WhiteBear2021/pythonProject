import sys
read=sys.stdin.readline

n, k = map(int, read().split())

bags = [[0,0]]
d = [[0]*(k+1) for _ in range(n+1)]

for i in range(n):
    bags.append(list(map(int, read().split())))

for i in range(1, n+1):
    for j in range(1, k+1):
        w = bags[i][0]
        v = bags[i][1]

        if j < w:
            d[i][j] = d[i-1][j]
            print(d)
        else:
            d[i][j] = max(d[i-1][j], d[i-1][j-w]+v)
            print(d)

print(d)
print(d[n][k])
