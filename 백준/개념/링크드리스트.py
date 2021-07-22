# 노드 : 칸에 있는 데이터, 다음 칸에 어떤 노드가 연결되어있는지
# 1.Node 클래스 만들기
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
# 2.링크드리스트 append print insert delete
# 링크드 리스트는 head에 노드만 가지고 있고 노드.next에 노드를 연결하여 리스트를 만든다
class LinkedList:
    def __init__(self,data):
        self.head=Node(data)
    
    # 링크드 리스트에 노드 추가
    def append(self,data):
        cur=self.head
        while cur.next is not None:
            cur=cur.next
        cur.next=Node(data)
    # 링크드 리스트 출력 
    def print_all(self):
        cur=self.head
        while cur is not None:
            print(cur.data)
            cur=cur.next
    # 링크드 리스트 index값으로 접근
    def get_node(self,index):
        node=self.head
        count=0
        while count<index:
            node=node.next
            count+=1
        return node
    
    # 링크드 리스트 index 위치에 값 추가
    def add_node(self,index,value):
        new_node=Node(value)
        if index==0:
            new_node.next=self.head
            self.head=new_node
            return
        node=self.get_node(index-1)
        next_node=node.next
        node.next=new_node
        new_node.next=next_node
    
    # index로 접근하여 원소 삭제하기
    def delete_node(self,index):
        if index==0:
           self.head=self.head.next
        node=self.get_node(index-1)
        node.next=node.next.next
    
list=LinkedList(5)
list.append(12)
list.append(6)
result=list.get_node(1).data
print(result)
list.add_node(2,7)
list.print_all()
list.delete_node(1)
list.print_all()

        