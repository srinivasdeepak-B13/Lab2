class Node:
    def __init__(self,data):
        self.next = None
        self.prev = None
        self.data = data
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def print_list(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next
d=DoublyLinkedList()
d.head = Node(10)
d.head.next=Node(20)
d.head.next.next=Node(30)
d.print_list()
