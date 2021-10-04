def solution(gems):
    answer = [0,0]
    n=len(set(gems))
    # print(n)
    max_len=1000000
    if n==1:
        answer = [1,1]
    else:
        for i in range(len(gems)):
            item_list=[gems[i]]
            if len(gems)-i==n:break
            for j in range(i+1,len(gems)):
                if j-i>=max_len:break
                if gems[j] not in item_list:
                    item_list.append(gems[j])
                # print(item_list)
                if len(item_list)==n:
                    max_len=j-i
                    answer[0]=i+1
                    answer[1]=j+1
    return answer

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
# gems	result
# ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]	[3, 7]
# ["AA", "AB", "AC", "AA", "AC"]	[1, 3]
# ["XYZ", "XYZ", "XYZ"]	[1, 1]
# ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]	[1, 5]