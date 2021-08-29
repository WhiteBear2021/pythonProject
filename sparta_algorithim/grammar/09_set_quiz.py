student_a = ['물리2','국어','수학1','음악','화학1','화학2','체육']
student_b = ['물리1','수학1','미술','화학2','체육']
# 교집합, 합집합, 차집합 set을 이용
a=set(student_a)
b=set(student_b)
print(a)
print(b)
a_b=(a&b)
print(a_b)
print(a-a_b)
