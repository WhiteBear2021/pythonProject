n=int(input())
input_list = [int(input()) for _ in range(n)]
input_list.sort(reverse=True)
max_weight=0
for i in range(len(input_list)):
    comp_weight=(i+1)*input_list[i]
    if max_weight<comp_weight:
        max_weight=comp_weight
print(max_weight)
