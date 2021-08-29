scores = [
    {'name':'영수','score':70},
    {'name':'영희','score':65},
    {'name':'기찬','score':75},
    {'name':'희수','score':23},
    {'name':'서경','score':99},
    {'name':'미주','score':100},
    {'name':'병태','score':32}
]
# str(숫자) => 문자로 변형 f-string은 f'{변수명}'
for s in scores:
    print(s)
    name=s['name']
    score=s['score']
    print(name,score)
    print(name+"의 점수는 "+str(score)+"입니다")
    print(f'{name}의 점수는 {score}입니다')