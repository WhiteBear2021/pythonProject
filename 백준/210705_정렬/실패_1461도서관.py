N,M=map(int, input().split())
loc_arr=list(map(int, input().split()))
a=max(loc_arr)
b=min(loc_arr)
total_move_distance=0
if N%M==0:
    loc_arr.sort()
else:
    if a>=abs(b):
        loc_arr.sort()
        loc=loc_arr.pop()
        change_loc=loc
        total_move_distance+=abs(loc)
        for _ in range(M-2):
            change_loc=loc_arr.pop()
            dis=loc-change_loc
            loc=change_loc
            total_move_distance+=abs(dis)
    else:
        loc_arr.sort(reverse=True)
        loc=loc_arr.pop()
        change_loc=loc
        total_move_distance+=abs(loc)
        for _ in range(M-2):
            change_loc=loc_arr.pop()
            dis=loc-change_loc
            loc=change_loc
            total_move_distance+=abs(dis)
            
print(f"처음 total distance{total_move_distance}")
print(loc_arr)

my_loc=0
for i in range(len(loc_arr)):
    if i!=0 and i%M==0:
        total_move_distance+=abs(my_loc)
        print(f"되돌아오는 거리 {abs(my_loc)}")
        print(f"총거리{total_move_distance}")
        my_loc=0
    print(f"현재위치 {my_loc}")
    print(f"가야하는위치 {loc_arr[i]}")
    distance=my_loc-loc_arr[i]
    print(f"거리{abs(distance)}")
    my_loc=loc_arr[i]
    total_move_distance+=abs(distance)
    print(f'총거리{total_move_distance}')
print(total_move_distance)