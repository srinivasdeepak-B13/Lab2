class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class BinaryTree:
    def __init__(self):
        self.root=None
b=BinaryTree()
b.root=Node(10)
print(b.root.data)
