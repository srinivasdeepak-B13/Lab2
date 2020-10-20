class Node:
    def __init__(self,data):
        self.next=None
        self.prev=None
        self.data=data
class DoublyLinkedList:
    def __init__(self):
        self.head=None
    def print_list(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next
    def append(self,data):
        if self.head is None:
            new=Node(data)
            self.head=new
        else:
            new=Node(data)
            cur=self.head
            while cur.next:
                cur=cur.next
            cur.next=new
            new.prev=cur
d=DoublyLinkedList()
d.append(10)
d.append(20)
d.append(30)
d.print_list()
