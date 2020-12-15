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
    def Max_min(self):
        if self.head is None:
            return
        if self.head.next==None:
            print("Max and Min are",self.head.data)
            return
        temp=self.head
        small=self.head.data
        large=self.head.data
        while temp:
            if temp.data>large:
                large=temp.data
            if temp.data<small:
                small=temp.data
            temp=temp.next
        print("Minimum in list is ",small)
        print("Maximum in list is ",large)
LL=SinglyLinkedList()
n=int(input("Enter no. of elements to append "))
for i in range(n):
    LL.append(int(input()))
LL.Max_min()
