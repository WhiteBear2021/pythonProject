# 이 전화 키패드에서 왼손과 오른손의 엄지손가락만을 이용해서 숫자만을 입력하려고 합니다.
# 맨 처음 왼손 엄지손가락은 * 키패드에 오른손 엄지손가락은 # 키패드 위치에서 시작하며, 엄지손가락을 사용하는 규칙은 다음과 같습니다.

# 엄지손가락은 상하좌우 4가지 방향으로만 이동할 수 있으며 키패드 이동 한 칸은 거리로 1에 해당합니다.
# 왼쪽 열의 3개의 숫자 1, 4, 7을 입력할 때는 왼손 엄지손가락을 사용합니다.
# 오른쪽 열의 3개의 숫자 3, 6, 9를 입력할 때는 오른손 엄지손가락을 사용합니다.
# 가운데 열의 4개의 숫자 2, 5, 8, 0을 입력할 때는 두 엄지손가락의 현재 키패드의 위치에서 더 가까운 엄지손가락을 사용합니다.
# 4-1. 만약 두 엄지손가락의 거리가 같다면, 오른손잡이는 오른손 엄지손가락, 왼손잡이는 왼손 엄지손가락을 사용합니다.
# 순서대로 누를 번호가 담긴 배열 numbers, 왼손잡이인지 오른손잡이인 지를 나타내는 문자열 hand가 매개변수로 주어질 때, 각 번호를 누른 엄지손가락이 왼손인 지 오른손인 지를 나타내는 연속된 문자열 형태로 return 하도록 solution 함수를 완성해주세요.

# [제한사항]

# numbers 배열의 크기는 1 이상 1,000 이하입니다.
# numbers 배열 원소의 값은 0 이상 9 이하인 정수입니다.
# hand는 "left" 또는 "right" 입니다.
# "left"는 왼손잡이, "right"는 오른손잡이를 의미합니다.
# 왼손 엄지손가락을 사용한 경우는 L, 오른손 엄지손가락을 사용한 경우는 R을 순서대로 이어붙여 문자열 형태로 return 해주세요.

# [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]

# 각번호에 대한 값을 좌표를 가지도록 값을 준다
# 좌표값의 차이가 이동거리가 되므로 오른손으로 누를지 왼손으로 누를지 정해줄 수 있다
num_arr={1:(1,1),2:(1,2),3:(1,3),
         4:(2,1),5:(2,2),6:(2,3),
         7:(3,1),8:(3,2),9:(3,3),
         "*":(4,1),0:(4,2),"#":(4,3)}

def solution(numbers, hand):
    answer = ''
    left=num_arr.get("*")
    right=num_arr.get("#")
    for num in numbers:
        if num in [1,4,7]:
            answer+="L"
            left=num_arr.get(num)
        elif num in [3,6,9]:
            answer+="R"
            right=num_arr.get(num)
        else:
            target=num_arr.get(num)
            gap_l=abs(left[0]-target[0])+abs(left[1]-target[1])
            gap_r=abs(right[0]-target[0])+abs(right[1]-target[1])
            if gap_l>gap_r:
                right=target
                answer+="R"
            elif gap_r>gap_l:
                left=target
                answer+="L"
            else:
                if hand=="left":
                    left=target
                    answer+="L"
                else:
                    right=target
                    answer+="R"
        print(num,left,right)
    return answer
    
print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right"))