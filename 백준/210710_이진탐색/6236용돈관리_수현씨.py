n, m = map(int, input().split())
k = [int(input()) for _ in range(n)]
left = min(k)
right = sum(k)
if n==m:
   print(max(k))
else:
    while left <= right:
        mid = (left+right)//2
        total = 0
        count = 1
        for i in k:
            if total+i >= mid:
                total += i
                count += 1
        if count+1 <= m:
            right = mid - 1
        else:
            left = mid + 1

    print(mid)