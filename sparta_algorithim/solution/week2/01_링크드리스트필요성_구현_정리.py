class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
# Node() 함수에 .data에는 데이터 값들어가도록, .next는 None 아무것도 저장되지 않도록 설정 해놓은 함수

node=Node(3)
print("node=Node(3)")
print("node.data값은:",node.data)
print("node.next값은:",node.next)


class LinkedList:
    def __init__(self,data):
        self.head=Node(data)

    def append(self,data):
        cur=self.head
        while cur.next is not None:
            cur=cur.next
        cur.next=Node(data)
        print("cur=self.head")
        print("cur의 값==>",cur)
        print("cur.data의 값==>",cur.data)
        print("cur.next의값 ==>",cur.next)
        print("cur.next.data의값 ==>", cur.next.data)
    def print_all(self):
        print("print_all 함수 실행!!")
        cur=self.head
        while cur is not None:
            print(cur.data)
            cur=cur.next

linked_list=LinkedList(3)
linked_list.append(4)
linked_list.append(5)
print("linked_list.head 값은:",linked_list.head)
print("linked_list.head.data 값은:",linked_list.head.data)
print("linked_list.head.next 값은:",linked_list.head.next)


linked_list.print_all()