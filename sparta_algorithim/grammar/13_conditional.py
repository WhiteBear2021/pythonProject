num =3
if num%2==0:
    result='짝수'
else:
    result="홀수"
    
print(f'{num}은 {result}입니다')

result=('짝수' if num%2==0 else '홀수')
print(f'{num}은 {result}입니다')

a_list=[1,3,2,5,1,2]
b_list=[]

for a in a_list:
    b_list.append(a*2)

print(b_list)

c_list=[]
c_list=[a*2 for a in a_list]
print(c_list)