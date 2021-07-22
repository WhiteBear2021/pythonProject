import time
s = time.time()
n = 50
for i in range(n):
    for j in range(n):
        print(i,j)
        # for _ in range(n):
            # print(i,j,_)
e = time.time()

print(e-s)