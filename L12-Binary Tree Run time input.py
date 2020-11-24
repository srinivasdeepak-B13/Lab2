class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class BinaryTree:
    def __init__(self):
        self.root=None
    def insert(self,data):
        cur=self.root
        prev=None
        while True:
            prev=cur
            if cur.data>data:
                if cur.left: cur=cur.left
                else:
                    cur.left=Node(data)
                    break
            else:
                if cur.right: cur=cur.right
                else:
                    cur.right=Node(data)
                    break
    def PrintTree(self,node):
        if node.left: self.PrintTree(node.left)
        print(node.data)
        if node.right: self.PrintTree(node.right)
        
b=BinaryTree()
d=int(input("Enter the value of root data "))
b.root=Node(d)
while True:
    k=input("Enter data you want to insert or quit for stopping insertion ")
    if k!="quit": b.insert(int(k))
    else: break
b.PrintTree(b.root)
