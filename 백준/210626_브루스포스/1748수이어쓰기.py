import sys
N=int(sys.stdin.readline())
n_length=len(str(N))-1
total_length=0
n=0
while n<n_length:
    total_length+=9*(10**n)*(n+1)
    n+=1

if n_length==0:
    total_length=int(N)
else:   
    total_length+=((int(N)-(10**(n_length)))+1)*(n_length+1)

print(total_length)