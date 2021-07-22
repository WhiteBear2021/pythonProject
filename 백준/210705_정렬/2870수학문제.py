import sys
N=int(sys.stdin.readline())

prob_arr=[]
result_arr=[]

for i in range(N):
   prob_arr.append(sys.stdin.readline()[:-1]) 
   
# print(prob_arr)

for str in prob_arr:
    result_num=""
    for _ in str:
        if _.isalpha():
            if result_num!="":
                result_arr.append(int(result_num))
            # print(f"{_}은 알파벳입니다.")
            result_num=""
        else:
            # print(f"{_}은 숫자입니다.")
            result_num=result_num+_
        # print(_)
    else:
        if result_num!="":
            result_arr.append(int(result_num))

result_arr.sort()
for val in result_arr:
    print(val)