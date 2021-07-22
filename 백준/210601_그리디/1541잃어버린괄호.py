
str_arr=input().split('-')
list=[]
for i in range(len(str_arr)):
    if '+' in str_arr[i]:
        plus_arr = str_arr[i].split('+')
        plus_val = 0
        for j in range(len(plus_arr)):
            plus_val += int(plus_arr[j])
    else:
        plus_val = 0
        plus_val = int(str_arr[i])
    list.append(plus_val)
result=list[0]
for j in range(1,len(list)):
    result-=list[j]
print(result)

# .isdigit()
# .ischar()
# .index('찾을문자')
# print(str.index('-'))
# print(eval(str[changing_idx:str.index('-')]))
# print(eval(str))



