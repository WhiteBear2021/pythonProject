def solution(genres, plays):
    answer = []
    music_dict={}
    total_cnt={}
    for i,(g,p) in enumerate(zip(genres,plays)):
        print(i,(g,p))
        music_dict[i]=(g,p)
        if total_cnt.get(g):
            total_cnt[g]+=p
        else:
            total_cnt[g]=p
    rate_arr=sorted(music_dict.items(), key = lambda item: item[1], reverse=True)
    total_cnt=sorted(total_cnt.items(), key = lambda item: item[1], reverse=True)
    # print(rate_arr)
    # print(music_dict)
    # print(total_cnt)
    for rank in total_cnt:
        kind=rank[0]
        cnt=0
        for r in rate_arr:
            if r[1][0]==kind:
                cnt+=1
                answer.append(r[0])
            if cnt==2:break
    return answer

genre=["classic", "pop", "classic", "classic", "pop"]
plays=[500, 600, 150, 800, 2500]