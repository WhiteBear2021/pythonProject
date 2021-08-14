def solution(v):
    answer = []
    x_dict={}
    y_dict={}
    for _ in range(3):
        x_val=v[_][0]
        y_val=v[_][1]
        if x_dict.get(x_val):
            x_dict[x_val]+=1
        else:
            x_dict[x_val]=1
        if y_dict.get(y_val):
            y_dict[y_val]+=1
        else:
            y_dict[y_val]=1
    for key,value in x_dict.items():
        if value==1:
            answer.append(key)
            break
    for key,value in y_dict.items():
        if value==1:
            answer.append(key)
            break
    return answer

print(solution([[1, 4], [3, 4], [3, 10]]))