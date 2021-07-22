import sys


height_arr = [int(sys.stdin.readline()) for i in range(9)]
total=sum(height_arr)
for i in range(9):
    for j in range(9):
        if i==j:continue
        if total-(height_arr[i]+height_arr[j])==100:
            num1,num2=height_arr[i],height_arr[j]
            height_arr.remove(num1)
            height_arr.remove(num2)
            height_arr.sort()
            for h in height_arr:
                print(h)
            break
    if len(height_arr)==7:break
            
