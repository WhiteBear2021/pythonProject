import sys
from itertools import permutations
import time
s = time.time()
height_arr=[]
for i in range(9):
    height_arr.append(int(sys.stdin.readline()))
    
print(height_arr)

new_h_arr=list(permutations(height_arr,7))
answer_arr=()
for k in new_h_arr:
    if sum(k)==100:
        k.sort()
        for a in k:
            print(a)
        break


    
e = time.time()

print(e-s)