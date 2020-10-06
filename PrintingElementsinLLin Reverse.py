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
    def print_reverse(self):
        temp=self.head
        s=[]
        while temp:
            s.append(temp.data)
            temp=temp.next
        for i in range(len(s)):
            print(s.pop())
LL=SinglyLinkedList()
n=int(input("Enter no. of elements to append "))
for i in range(n):
    LL.append(int(input()))
print("printing in reverse")
LL.print_reverse()
