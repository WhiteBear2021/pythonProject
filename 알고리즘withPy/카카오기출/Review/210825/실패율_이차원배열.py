# 실패율은 다음과 같이 정의한다.
# 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
# 전체 스테이지의 개수 N, 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages가 매개변수로 주어질 때, 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 return 하도록 solution 함수를 완성하라.

# 제한사항
# 스테이지의 개수 N은 1 이상 500 이하의 자연수이다.
# stages의 길이는 1 이상 200,000 이하이다.
# stages에는 1 이상 N + 1 이하의 자연수가 담겨있다.
# 각 자연수는 사용자가 현재 도전 중인 스테이지의 번호를 나타낸다.
# 단, N + 1 은 마지막 스테이지(N 번째 스테이지) 까지 클리어 한 사용자를 나타낸다.
# 만약 실패율이 같은 스테이지가 있다면 작은 번호의 스테이지가 먼저 오도록 하면 된다.
# 스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0 으로 정의한다.

# 스테이지갯수, 각 참가자들이 진행중인 스테이지를 나타내는 배열 
def solution(N, stages):
    answer = []
    # 총 인원 수 ppl_num
    ppl_num=len(stages)
    # (스테이지번호,실패율)을 담을 것이다.
    failure_list=[]
    for i in range(1,N+1):
        num=stages.count(i)
        if ppl_num==0:
            fail_rate=0
        else:
            fail_rate=num/ppl_num
        failure_list.append((i,fail_rate))
        ppl_num-=num
    failure_list.sort(key=lambda x:(-x[1],x[0]))
    answer=[fail[0] for fail in failure_list]
# ---------------------------------------------------
    # # stage번호당 인원수 cnt
    # cnt=[0]*(N+1)
    # for stage in stages:
    #     for i in range(1,len(cnt)):
    #         if stage==i:
    #             cnt[i]+=1
    # # stage번호와 성공률을 담을 list
    # failure_list=[]
    # for c in range(1,len(cnt)):
    #     if ppl_num==0:
    #         f_rate=0
    #     else:
    #         # 실패율
    #         f_rate=cnt[c]/ppl_num
    #         # 다음단계로 갈때 인원수 빼준다
    #         ppl_num-=cnt[c]
    #     # 실패률, 단계 튜플로 넣는다
    #     failure_list.append((f_rate,c))
    # # 실패율 높은순으로 정렬, 동일 실패율 번호 오름차순
    # failure_list.sort(key=lambda x: (-x[0], x[1]))
# ------------------------------------------------------------
    # for t in failure_list:
    #     answer.append(t[0])
    return answer

print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))