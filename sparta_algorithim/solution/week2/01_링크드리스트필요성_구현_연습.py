# data, next
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

node=Node("3")
print(node)
print(node.data)
print(node.next)

# [3]->[4]->[5]->[6] append() 이용해서 만들기
class LinkedList:
    def __init__(self,data):
        self.head=Node(data)
    def append(self,data):
        cur=self.head
        while cur.next is not None:
            cur=cur.next
        cur.next=Node(data)
        print(cur.data)
        print(cur.next.data)
    def print_all(self):
        pass

linklist=LinkedList("3")
print(linklist.head.data)
linklist.append("4")
linklist.append("5")





