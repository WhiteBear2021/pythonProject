# A: 걸, B : 개, C : 도, D : 윷, E : 모
yut_dict={0:"D",1:"C",2:"B",3:"A",4:"E"}
answer=[]
for _ in range(3):
    yuts=list(map(int,input().split()))
    val=sum(yuts)
    ans=yut_dict.get(val)
    answer.append(ans)
for a in answer:
    print(a)