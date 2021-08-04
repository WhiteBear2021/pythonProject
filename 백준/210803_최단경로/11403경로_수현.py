n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        for k in range(n):
            if matrix[j][i] and matrix[i][k]:
                matrix[j][k]=1
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=' ')
    print()