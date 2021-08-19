array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]

# 정렬된 두 배열 a, b가 있을 때, 두 개를 합쳐서 정렬하기
def merge(array1, array2):
    # 이 부분을 채워보세요!
    idx1=0
    idx2=0
    new_array=[]
    while idx1<len(array1) and idx2<len(array2):
        if array1[idx1]<array2[idx2]:
            new_array.append(array1[idx1])
            idx1+=1
        else:
            new_array.append(array2[idx2])
            idx2+=1
        if idx1==len(array1):
            new_array+=array2[idx2:]
            idx2=len(array2)
        if idx2==len(array2):
            new_array+=array1[idx1:]
            idx1=len(array1)
    return new_array


print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!