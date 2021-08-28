import collections


from itertools import combinations
# new_h_arr=list(combinations(m,6))
a= ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
b=[2,3,4]

def solution(orders, course):
    answer = []
    # 사람 시킨 음식들 orders
    orders.sort(key=lambda x:len(x))
    print(orders)
    # 코스 요리 갯수(2명이상 주문해야 가능)
    for i in course:
        print(i)
        for order in orders:
            if len(order)==i:
                for m in orders:
                    if len(m)<i:continue
                    count=0
                    for s in m:
                        for s1 in order:
                            if s==s1:
                                count+=1
                        if count==i:
                            if answer and answer[-1]==order: break
                            answer.append(order)
                            break
                        
    
    
    
    
    # menu_dict={}
    # for menu in orders:
    #     for m in menu:
    #         if menu_dict.get(m):
    #             menu_dict[m]+=1
    #         else:
    #             menu_dict[m]=1 
    # print(menu_dict)
    
    
    # # 주문한 사람 갯수에 따른 alphabet 넣기
    # menu_list=[""]*(len(orders)+1)
    # for k in menu_dict.keys():
    #     idx=menu_dict[k]
    #     menu_list[idx]+=k
    # print(menu_list)
    
    # menu_list=sorted(menu_dict.items(), key=lambda item:item[0])
    # print(menu_list)
    # rate_arr=sorted(rate_dict.items(), key = lambda item: item[1], reverse=True)
    # for i in course:
    #     new_list=list(combinations(menu_list[0],i))
    #     print(new_list)
    return answer

print(solution(a,b))