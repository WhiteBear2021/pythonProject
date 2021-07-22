import sys
N=int(sys.stdin.readline())
s=set()
# s.update(값)
# s.remove(값)
# 모든 요소 제거 s.clear()
# 값 in s
for i in range(N):
    arr=list(sys.stdin.readline().split())
    if arr[0]=="add":
        s.update(arr[1])
    elif arr[0]=="remove":
        s.discard(arr[1])
    elif arr[0]=="check":
        if arr[1] in s:
            print(1)
        else:
            print(0)
    elif arr[0]=="toggle":
        if arr[1] in s:
            s.remove(arr[1])
        else:
            s.update(arr[1])
    elif arr[0]=="all":
        s.update({"1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"})
    elif arr[0]=="empty":
        s.clear()
