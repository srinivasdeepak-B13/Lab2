class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SinglyLinkedList:
    def __init__(self):
        self.head=None
    def append(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=new_node
    def print_list(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next
    def delete_last_node(self):
        temp=self.head
        if self.head.next==None:
            self.head=None
            return
        prev=None
        while temp.next:
            prev=temp
            temp=temp.next
        prev.next=None
LL=SinglyLinkedList()
n=int(input("Enter no. of elements to append "))
for i in range(n):
    LL.append(int(input()))
print("deleting last node ")
LL.delete_last_node()
LL.print_list()
