n = int(input())
a = list(map(int, input().split()))

def next_permutation(a):
    n=len(a)-1
    i = n
    while i>0 and a[i-1]>=a[i]:
        i-=1
       
    #만약 i가 0이라면 리스트가 완벽한 내림차순이므로 False리턴
    if i==0:
        return False
        
    #값을 swap
    j = n
    while a[i-1]>=a[j]:
        j-=1
    a[i-1],a[j]=a[j],a[i-1]
    
    #i이후의 값들을 정렬(=끝에서부터 앞의 수와 차례로 swap)
    j=n
    while i<j:
        a[i],a[j]=a[j],a[i]
        i+=1
        j-=1
    return True

if next_permutation(a) is True:
    for i in a:
        print(i, end=' ')
    print()
else:
    print(-1)

   