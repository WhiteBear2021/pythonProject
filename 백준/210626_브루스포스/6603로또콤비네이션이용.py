from itertools import combinations

while True:
    map_list = list(map(int, input().split()))
    if map_list[0]==0:break
    a=map_list[1:]
    # a.sort()
    
# print(arr)    
    new_h_arr=list(combinations(a,6))
    for v in new_h_arr:
        print(v[0],v[1],v[2],v[3],v[4],v[5])
    print()   
