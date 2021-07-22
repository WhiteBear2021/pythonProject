N,M=map(int, input().split())
loc_arr=list(map(int, input().split()))
neg_loc_arr=[]
pos_loc_arr=[]
final_distance=0
for val in loc_arr:
    if val<0:
        neg_loc_arr.append(val)
    else:
        pos_loc_arr.append(val)
if len(neg_loc_arr)>0:
    neg_loc_arr.sort()
    final_distance=abs(neg_loc_arr[0])
if len(pos_loc_arr)>0:
    pos_loc_arr.sort(reverse=True)
    final_distance=pos_loc_arr[0]
if len(neg_loc_arr)>0 and len(pos_loc_arr)>0:
    if abs(neg_loc_arr[0])>pos_loc_arr[0]:
        final_distance=abs(neg_loc_arr[0])
    else:
        final_distance=pos_loc_arr[0]
print(neg_loc_arr)
print(pos_loc_arr)

total_move_distance=0
for idx in range(len(neg_loc_arr)):
    if idx%M==0:
        total_move_distance+=abs(neg_loc_arr[idx])*2
        
for idx in range(len(pos_loc_arr)):
    if idx%M==0:
        total_move_distance+=pos_loc_arr[idx]*2
        
total_move_distance-=final_distance
print(total_move_distance)


        
    
