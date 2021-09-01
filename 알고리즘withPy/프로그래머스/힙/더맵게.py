import heapq
def solution(scoville, k):
    heap = []
    for num in scoville:
        heapq.heappush(heap, num)
        mix_cnt = 0
    while heap[0] < k:
        try:
            heapq.heappush(heap, heapq.heappop(heap) + (heapq.heappop(heap) * 2))
        except IndexError:
            return -1
        mix_cnt += 1
    return mix_cnt

# scoville	K	return
# [1, 2, 3, 9, 10, 12]	7	2
arr=[1, 2, 3, 9, 10, 12]
num=7
print(solution(arr,num))