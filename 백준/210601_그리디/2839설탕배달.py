weight=int(input())
a,b=divmod(weight,5)
c,d=divmod(b,3)
if d==0:
    print(a+c)
elif not d==0:
    for i in range(a,-1,-1):
        e,f=divmod(weight-(5*i),3)
        if f==0:
            print(i+e)
            break
    else:
        print(-1)
