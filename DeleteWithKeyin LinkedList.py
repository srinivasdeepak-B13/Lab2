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
    def delete_with_key(self,key):
        temp=self.head
        prev=None
        if self.head is None:
            return
        elif self.head.data==key:
            self.head=temp.next
            temp=None
            return
        else:
            while temp:
                if temp.data==key:
                    break
                prev=temp
                temp=temp.next
            prev.next=temp.next
            temp=None
            return
                
LL=SinglyLinkedList()
n=int(input("Enter no. of elements to append "))
for i in range(n):
    LL.append(int(input()))
k=int(input("Enter the key to delete "))
LL.delete_with_key(k)
LL.print_list()
        
