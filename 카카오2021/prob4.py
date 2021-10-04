from bisect import bisect_right, bisect_left

def solution(n, info):

    sum_a = sum([10-i for i, x in enumerate(info) if x != 0])
    print(sum_a)

    for idx, value in enumerate(info):
        if value == 1:
            info[idx] = 2
        elif value == 2:
            info[idx] = 0
    sum_b = sum(list(filter(lambda x: x > 0, info)))
    answer = []
    return answer


print(solution(5,[2,1,1,1,0,0,0,0,0,0,0]))
# n   info   result
# 5   [2,1,1,1,0,0,0,0,0,0,0]   [0,2,2,0,1,0,0,0,0,0,0]
# 1   [1,0,0,0,0,0,0,0,0,0,0]   [-1]
# 9   [0,0,1,2,0,1,1,1,1,1,1]   [1,1,2,0,1,2,2,0,0,0,0]
# 10   [0,0,0,0,0,0,0,0,3,4,3]   [1,1,1,1,1,1,1,1,0,0,2]