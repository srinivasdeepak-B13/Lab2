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
    def PreOrder(self,node):
        print(node.data)
        if node.left: self.PreOrder(node.left)
        if node.right: self.PreOrder(node.right)
    def InOrder(self,node):
        if node.left: self.InOrder(node.left)
        print(node.data)
        if node.right: self.InOrder(node.right)
    def PostOrder(self,node):
        if node.left: self.PostOrder(node.left)
        if node.right: self.PostOrder(node.right)
        print(node.data)
b=BinaryTree()
d=int(input("Enter the value of root data "))
b.root=Node(d)
while True:
    k=input("Enter data you want to insert or quit for stopping insertion ")
    if k!="quit": b.insert(int(k))
    else: break
print("Preorder Traversal ")
b.PreOrder(b.root)
print("Inorder Traversal ")
b.InOrder(b.root)
print("Postorder Traversal ")
b.PostOrder(b.root)
