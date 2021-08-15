from itertools import permutations

# 카드 갯수 N
# 뽑을 카드 갯수 K
N=int(input())
K=int(input())

# 뽑은 카드 리스트
card_list=[input() for _ in range(N)]
card_K=list(permutations(card_list,K))
# print(card_K)
# print(N,K,card_list)

card_K_set=set()
for card_k in card_K:
    card=""
    for k in range(K):
        card+=card_k[k]
    card_K_set.add(card)
    
print(len(card_K_set))