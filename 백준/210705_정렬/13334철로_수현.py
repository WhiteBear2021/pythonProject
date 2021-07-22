import sys
n = int(sys.stdin.readline())
location = []
for _ in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    tmp.sort()
    location.append(tmp)
d = int(sys.stdin.readline())
max = 0

location.sort()
for i in location:
    people = 0
    a = i[0]
    for j in location:
        if j[0]>=a and j[1]<=a+d:
            people+=1
    if people> max:
        max = people
print(max)