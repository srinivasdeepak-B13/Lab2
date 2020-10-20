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
    def prepend(self,data):
        if self.head is None:
            new=Node(data)
            new.next=self.head
            self.head=new
        else:
            new=Node(data)
            self.head.prev=new
            new.next=self.head
            self.head=new
d=DoublyLinkedList()
d.prepend(10)
d.prepend(20)
d.prepend(30)
d.print_list()
