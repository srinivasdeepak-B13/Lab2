class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class BinaryTree:
    def __init__(self):
        self.root=None
    def insert(self,data):
        if self.root is None:
            self.root=Node(data)
            return
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
        if node.left:
            self.PrintTree(node.left)
        print(node.data)
        if node.right:
            self.PrintTree(node.right)
b=BinaryTree()
b.insert(100)
b.insert(50)
b.insert(120)
b.insert(30)
b.insert(60)
b.insert(20)
b.insert(35)
b.insert(45)
b.insert(95)
b.insert(105)
b.insert(300)
b.insert(400)

b.PrintTree(b.root)


