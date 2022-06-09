class Node:
    def __init__(self,val):
        self.val=val
        self.rchild=None
        self.lchild=None
def height(node):
    if node is None:
        return 0
    return 1+max(height(node.lchild), height(node.rchild))
def diameter(root):
    if root is None:
        return 0
    #height of left amd right subtree
    lheight=height(root.lchild)
    rheight=height(root.rchild)
    #diameter of left and right
    ldiameter=diameter(root.lchild)
    rdiameter=diameter(root.rchild)
    return max(lheight+rheight,max(ldiameter,rdiameter))
root = Node(1)
root.lchild = Node(2)
root.rchild = Node(3)
root.lchild.lchild = Node(4)
root.lchild.rchild = Node(5)
print(height(root))
print(diameter(root))