
# 1. 인자로 입력한 인자 이름을 써서 함수를 실행시켜주면 인자 순서 상관없이 가능
def cal(a,b):
    return a+2*b
result=cal(b=2,a=1)
print(result)

# 2. 기본값 설정, 값 넣어주면 넣어주는 값으로
def cal2(a,b=2):
    return a+2*b
result2=cal2(1)
print(result2)
result3=cal2(1,3)
print(result3)

# 3. 인자를 무제한으로 넣어줄 수 있다(list로 들어감)
def cal3(*args):
    for name in args:
        print(f'{name} 밥먹어라')

cal3("영수",'철수','미희')

# 4. 키워드 인수를 여러개
def cal4(**kwargs):
    print(kwargs)

cal4(name='bob',age=30,height=180)