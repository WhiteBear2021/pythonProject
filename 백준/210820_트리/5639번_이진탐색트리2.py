# 1처럼 트리를 이용하여 코드를 구현하면 시간초과가 난다.

# 이진트리를 만드는데 O(NlogN)

# 후위순회를 하는데 O(NlogN)의 시간이 든다.

# 트리를 만들지 않고 바로 출력하는 방식으로 만들어야겠다.

# 이진트리의 전위순회를 살펴보면

# 첫번째 루트 노드를 기준으로 작은값은 왼쪽 큰값은 오른쪽으로 나뉘는것을 볼 수 있다.

# 50 / 30 24 5 28 / 45 98 52 60

# 이렇게 분할하여 문제를 해결할수있다.



def postorder(start,end):
    if start>end:
        return
 
    division=end+1#나눌위치
    for i in range(start+1,end+1):
        if post[start]<post[i]:
            division=i
            break
 
    postorder(start+1,division-1)#분할 왼쪽
    postorder(division,end)#분할 오른쪽
    print(post[start])
 
 
 
import sys
sys.setrecursionlimit(10**9)
 
 
post=[]
count = 0
while count <= 10000:
    try:
        num = int(input())
    except:break
    post.append(num)
    count += 1
 
postorder(0,len(post)-1)