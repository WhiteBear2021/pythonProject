finding_target = 2
finding_numbers = [0, 3, 5, 6, 1, 2, 4]

def is_exist_target_number_binary(target, numbers):
    find_count=0
    for number in numbers:
        find_count+=1
        if number==target:
            print(find_count)
            return True
    return False


result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)