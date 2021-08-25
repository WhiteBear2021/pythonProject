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
    all_player=len(stages)
    # 실패율을 스테이지번호:실패율 key:value 형식으로 딕셔너리 자료구조에 담는다.
    # 나중에 딕셔너리 구조를 실패율 내림차순으로 sort하고 동일할 경우 스테이지번호가 낮은 것 부터 answer 배열에 넣을 수 있도록한다.
    rate_dict={}
    # 1~N까지의 스테이지를 count해서 진행중인스테이지인원수(즉 실패한 인원)/총인원(단계올라갈수록 이전단계 진행중인 인원을 빼주면 된다)
    for i in range(1,N+1):
        # allplayer가 0일 때 나누기를 못하니까 예외처리를 해준다. 이 때의 실패율은 0
        if all_player==0:
            fail_rate=0
        else:
            # 1~n을 stages배열에서 카운트한다
            cnt=stages.count(i)
            fail_rate=cnt/all_player
        # 1~n 까지의 스테이지번호:실패율을 넣는다
        rate_dict[i]=fail_rate
        # 낮은 스테이지를 진행하는 인원을 총 인원에서 빼준다
        all_player-=cnt
    print(rate_dict)
    rate_arr=sorted(rate_dict.items(), key = lambda item: item[1], reverse=True)
    print(rate_arr)
    answer=[fail[0] for fail in rate_arr]
    return answer

print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))