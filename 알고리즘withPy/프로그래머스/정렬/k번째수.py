def solution(array, commands):
    answer = []
    for command in commands:
        first=command[0]-1
        last=command[1]
        target=command[2]-1
        arr=array[first:last]
        arr.sort()
        print(arr)
        answer.append(arr[target])
    return answer

# array	commands	return
# [1, 5, 2, 6, 3, 7, 4]	[[2, 5, 3], [4, 4, 1], [1, 7, 3]]	[5, 6, 3]