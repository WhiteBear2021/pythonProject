class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

print(Node(3).data)

class LinkedList:
    def __init__(self,data):
        self.head=Node(data)
    def append(self,data):
        cur=self.head
        while cur.next is not None:
            cur=cur.next
        cur.next=Node(data)
    def print_all(self):
        cur=self.head
        while cur is not None:
            print(cur.data)
            cur=cur.next


linklist=LinkedList(3)
linklist.append(4)
linklist.append(5)
linklist.append(6)
linklist.append(7)
linklist.print_all()