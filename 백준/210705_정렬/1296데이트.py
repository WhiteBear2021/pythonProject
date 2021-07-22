import sys

cnt_L=0
cnt_O=0
cnt_V=0
cnt_E=0
# 오민식 이름 받기 name
name=sys.stdin.readline()
for c in name:
    if c=="L":
        cnt_L+=1
    elif c=="O":
        cnt_O+=1
    elif c=="V":
        cnt_V+=1
    elif c=="E":
        cnt_E+=1
    else:
        continue
# print(cnt_L,cnt_O,cnt_V,cnt_E)

# 여자 수
N=int(sys.stdin.readline())
women_arr = list(sys.stdin.readline()[:-1] for i in range(N))    
LOVE_arr=[0]*4
# print(women_arr)
women_arr.sort()
max_score=0
max_name=women_arr[0]
for i in range(len(women_arr)):
   LOVE_arr[0]=cnt_L 
   LOVE_arr[1]=cnt_O
   LOVE_arr[2]=cnt_V
   LOVE_arr[3]=cnt_E
   for j in women_arr[i]:
        if j=="L":
            LOVE_arr[0]+=1
        elif j=="O":
            LOVE_arr[1]+=1
        elif j=="V":
            LOVE_arr[2]+=1
        elif j=="E":
            LOVE_arr[3]+=1
        else:
            continue
#    print(LOVE_arr)
   score=1
   for q in range(len(LOVE_arr)):
       for k in range(q+1,len(LOVE_arr)):
          score*=(LOVE_arr[q]+LOVE_arr[k])
#    print(score)
   score=score%100
#    print(score,women_arr[i])
   if score>max_score:
        max_score=score
        max_name=women_arr[i]
        
print(max_name)