input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    value=input[0]
    for num in array:
        if value<= num:
            value=num
    return value


result = find_max_num(input)
print(result)