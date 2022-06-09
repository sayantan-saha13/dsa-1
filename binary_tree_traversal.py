class Binary_tree:
    def __init__(self,val):
        self.val=val
        self.right=None
        self.left=None
def inorder(Node):
    if Node:
        inorder(Node.left)
        print(Node.val,end=" ")
        inorder(Node.right)
def postorder(Node):
    if Node:
        postorder(Node.left)
        postorder(Node.right)
        print(Node.val,end=" ")
def preorder(Node):
    if Node:
        print(Node.val,end=" ")
        preorder(Node.left)
        preorder(Node.right)
root = Binary_tree(1)
root.left = Binary_tree(2)
root.right= Binary_tree(3)
root.left.left = Binary_tree(4)
root.left.right = Binary_tree(5)
root.right.right=Binary_tree(6)
root.right.right.right= Binary_tree(7)
print("tree traversal for inorder:")
inorder(root)
print("\npostorder traversal: ")
postorder(root)
print("\npreorder traversal: ")
preorder(root)
