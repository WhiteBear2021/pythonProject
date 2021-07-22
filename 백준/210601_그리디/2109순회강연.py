n=int(input())
mylist=[list(map(int, input().split())) for _ in range(n)]
mylist.sort(key=lambda x:(x[1],-x[0]))
if n==0:
    print(0)
else:
    new_arr=[]
    for i in range(n):
        d=mylist[i][1]
        if d>len(new_arr):
            new_arr.append(mylist[i][0])
            new_arr.sort()
        else:
            for j in range(len(new_arr)):
                if mylist[i][0]>new_arr[j]:
                    new_arr[j]=mylist[i][0]
                    break
    
    print(mylist)
    print(new_arr)
    print(sum(new_arr))