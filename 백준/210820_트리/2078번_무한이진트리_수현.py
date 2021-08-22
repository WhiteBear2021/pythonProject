L, R = map(int, input().split())
left, right = 0,0

while True:
    if L == 1:
        right += (R-1)
        break
    elif R == 1:
        left += (L-1)
        break
    elif L > R:
        left+=L//R
        L = L%R
    else:
        right+=R//L
        R = R%L
print(left, right)