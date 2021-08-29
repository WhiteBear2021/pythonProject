class MaxHeap:
    def __init__(self):
        self.items = [None]
    #     처음에 None값을 넣어주고 부모노드 //2, 왼쪽자식 *2, 오른쪽 자식 *2+1

    def insert(self, value):
        self.items.append(value)
        cur_index=len(self.items)-1

        while cur_index>1:
            parent_index=cur_index//2
            if self.items[cur_index]>self.items[parent_index]:
                self.items[cur_index],self.items[parent_index]=self.items[parent_index],self.items[cur_index]
                cur_index=parent_index
            else:
                break;
        return


max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!