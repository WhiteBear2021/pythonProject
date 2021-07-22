n=0
# 5 8 20
result_list=[]
while True:
    n+=1 
    vacation_days=0
    arr = list(map(int, input().split()))
    if arr[0]==0 and arr[1]==0 and arr[2]==0:break
    repeat_cnt=arr[2]//arr[1]
    # 2.xx->2
    vacation_days+=repeat_cnt*arr[0]
    # 5*2=10
    if arr[0]>=(arr[2]-(arr[1]*repeat_cnt)):#5 20-16
        vacation_days+=arr[2]-(arr[1]*repeat_cnt)
    else:
        vacation_days+=arr[0]
    result_list.append({"n":n,"vacation_days":vacation_days})

for result in result_list:    
    print("Case {0}: {1}".format(result.get("n"),result.get("vacation_days")))
