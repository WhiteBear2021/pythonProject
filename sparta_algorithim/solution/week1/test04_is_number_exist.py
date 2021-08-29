input = [3, 5, 6, 1, 2, 4]


def is_number_exist(number, array):
    for element in array: #-array의 길이 만큼 아래의 연산이 실행
        if number==element: #-비교연산 1번 실행
            return True     # N*1=N 만큼
    return False            # but 운이 좋으면 1번만에 배열의 첫번째에 3이 있으므로
                            # 운이 좋지않으면 배열의 뒷부분이 3이 존재한다면 오래 걸린다
                            # 입력값의 분포에 따라서 성능이 좌우 될 수 있다!
result = is_number_exist(3, input)
print(result)