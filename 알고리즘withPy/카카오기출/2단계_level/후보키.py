from itertools import combinations
r=[["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]

def solution(relation):
    answer = 0
    idx=len(relation[0])
    candidate_idx=[]
    for i in range(idx):
        val=[]
        for r in relation:
            if r[i] in val:
                break
            val.append(r[i])
        candidate_idx.append(i)
    print(candidate_idx)
    relation_idx=[i for i in range(len(relation[0])) if i not in candidate_idx]
    for n in range(2,len(relation[0])):
        if len(relation_idx)<n:
            return answer
        pair=list(combinations(relation_idx,n))
        print(pair)
    return answer

solution(r)