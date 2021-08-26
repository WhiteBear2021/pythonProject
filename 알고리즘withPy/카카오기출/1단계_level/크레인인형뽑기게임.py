# [제한사항]
# board 배열은 2차원 배열로 크기는 "5 x 5" 이상 "30 x 30" 이하입니다.
# board의 각 칸에는 0 이상 100 이하인 정수가 담겨있습니다.
# 0은 빈 칸을 나타냅니다.
# 1 ~ 100의 각 숫자는 각기 다른 인형의 모양을 의미하며 같은 숫자는 같은 모양의 인형을 나타냅니다.
# moves 배열의 크기는 1 이상 1,000 이하입니다.
# moves 배열 각 원소들의 값은 1 이상이며 board 배열의 가로 크기 이하인 자연수입니다.
# 입출력 예
# board	moves	result
# [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]	[1,5,3,5,1,2,1,4]	4

def solution(board, moves):
    answer = 0
    # moves 위치 index에 인형들 배치시키기
    board=[[]]+board
    # 뽑은 인형을 저장할 list : stack
    stack=[]
    for m in moves:
        for i in range(len(board[m])-1,-1,-1):
            val=board[m][i]
            if val!=0:
                # 인형뽑기 칸이 0이 아닐 때를 찾아서 뽑아주고(0으로 처리) 
                # stack에 인형이 들어있으면 먼저 들어있는 것과 번호가 같은지 비교하여 제거 후 answer+=2
                # 아니면 인형을 stack에 넣어준다
                board[m][i]=0
                if stack:
                    if val==stack[-1]:
                        print(val,stack[-1],'폭발')
                        stack.pop()
                        answer+=2
                    else:
                        stack.append(val)
                else:
                    stack.append(val)
                break
            elif sum(board[m])==0:
                print(m,"번 인형뽑기칸 비어있음")
                break
        print(board)
        print("stack 상태:",stack)
    print(board)
    
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))