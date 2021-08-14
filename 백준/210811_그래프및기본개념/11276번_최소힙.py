import sys, heapq

# 받을 값의 갯수 N
N=int(sys.stdin.readline())
q=[]
# 숫자 x를 받을 건데, 자연수를 입력 받을 때는 그 값을 넣고, 0을 입력 받을 때는 배열에서 최댓값을 제거하고 출력해준다, 배열이 비어있을 때는 0을 출력
for _ in range(N):
    # 받는 값 x
    x=int(sys.stdin.readline())
    if x==0:
        val=0
        if q:
            val=-heapq.heappop(q) 
        print(val)
        # print(f"정답은 {val}")
    else:
        heapq.heappush(q,-x)       