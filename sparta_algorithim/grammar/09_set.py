a=[1,2,3,4,5,6,7,89,1,42,4]

a_set=set(a)
print(a_set)

# set()은 중복을 제거해준다

a=['사과','감','배','수박','딸기']
b=['배','사과','포도','참외','수박']

a_set=set(a)
b_set=set(b)

# 교집합
print(a_set & b_set)
# 합집합
print(a_set | b_set)
