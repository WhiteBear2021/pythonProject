import sys
sys.setrecursionlimit(10**9)
array=[7,5,9,0,3,1,6,2,4,8]
# quick 정렬 정의 (정렬할배열,시작하는index,끝index)
def quick_sort(array,start,end):
  if start>=end:
    return
  # 기준데이터 pivot 첫번째값으로 설정
  pivot=start
  left=start+1
  right=end
  # index 왼쪽이 오른쪽보다 크거나 같을 때 while문 빠져나와서 pivot값을 기준으로 왼쪽 오른쪽을 퀵정렬할 것이다.
  while (left<=right):
    # 2.왼쪽에서 부터 pivot보다 큰 데이터 찾기 (작으면 while문 돌면서 left의 index값을 올려준다)
    while (left<=end and array[left]<=array[pivot]):
      left+=1
    # 3.오른쪽에서 부터 pivot보다 작은 데이터 찾기(데이터가 크면 while문 돌면서 right의 index값을 낮춰준다)
    while (right>start and array[right]>=array[pivot]):
      right-=1
    # 4.이전 2,3과정에서 왼쪽의 pivot보다 큰 데이터와 오른쪽의 작은 데이터를 change(우리는 현재 오름차순을 정렬할 것이기 때문에 왼쪽에 작은 데이터 오른쪽에 큰데이터가 오도록 할 것이다)
    # 4를 시행하기 위한 조건 : left와 right index가 엇갈리지않았다면(원래 left index가 right index보다 작아야함) 
    if left<right:
      array[left],array[right]=array[right],array[left]
    # 6.만약 left와 right index가 엇갈렸다면, 이 때 pivot값과 (left보다 index가 작은)pivot데이터보다 작은 데이터를 가진 right에 있는 값의 위치를 바꿔준다, 이렇게 하면 pivot을 기준으로 왼쪽은 작은값들이 모이고, 오른쪽은 큰값들이 모인다
    else:
      array[pivot],array[right]=array[right],array[pivot]
  # left와 right 인덱스가 엇갈리게 되면(left>right)이면 제일 큰 pivot과 left 위치가 바뀌게 될 것이고, while문 또한 빠져나올 것이다.
  # while문을 빠져나오면 pivot값을 기준으로 왼쪽값들과 오른쪽값들을 각각 퀵정렬 해주면된다(재귀함수 호출)
  quick_sort(array,start,right-1)
  quick_sort(array,right+1,end)

quick_sort(array,0,len(array)-1)
print(array)