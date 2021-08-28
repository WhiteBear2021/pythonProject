from itertools import combinations

def solution(orders, course):
    answer = []
    # index:길이안에 dict으로 {메뉴:반복횟수} 담을 리스트
    foodMap=[{} for _ in range(11)]
    # index:길이 마다 최대 주문횟수를 저장시켜놓음
    # 동일한 최대 주문일 때 둘다 출력하기 위해
    maxCnt=[0 for _ in range(11)]
    # 주문받은것들을 한사람마다 주문을 확인
    for order in orders:
        # 메뉴를 두 개 이상 부터 세트 메뉴를 만들 수 있기 때문에 2~그사람이시킨메뉴수 만큼 반복하면서
        for num in range(2,len(order)+1):
            # 그만큼 갯수를 순열로 combination 함수를 잉용해 튜플로 뽑은 다음, 
            # 문자열의 join 함수를 이용하여 그 순열 결과를 문자열로 합쳐준다.
            for i in combinations(sorted(order),num):
                print(i)
                key="".join(i)
                print(key)
                # foodMapd의 index에 해당되는 문자열이 있으면,
                # 그 때 문자열 횟수에서 +1 해주고
                # 없으면 그 때 문자열을 키값으로 하는 dic에 초기화(1을 넣어준다)
                # foodMap[배열idx][dic의키값]
                # 배열idx : 메뉴 갯수(문자열 길이), dic의 키값 : 메뉴조합
                if key in foodMap[num]:
                    foodMap[num][key]+=1
                    print(foodMap)
                    print(foodMap[num][key])
                    print(maxCnt)
                    maxCnt[num]=max(maxCnt[num],foodMap[num][key])
                else:
                    foodMap[num][key]=1
    for num in course:
        for k,v in foodMap[num].items():
            if v>=2 and v==maxCnt[num]:
                answer.append(k)
    return sorted(answer)

a= ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
b=[2,3,4]
print(solution(a,b))