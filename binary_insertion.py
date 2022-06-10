class Bst:
    def __init__(self,val):
        self.val=val
        self.right=None
        self.left=None
    def insert(self,data):
        if self.val==None:
            self.val=data
            return
        if self.val==data:
            return
        if self.val>data:
            if self.left:
              self.left.insert(data)
            else:
                self.left=Bst(data)
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = Bst(data)
    def search(self,data):
        if self.val==data:
            print("node is found")
            return
        if self.val>data:
            if self.left:
              self.left.search(data)
            else:
                print("node not found")
        else:
            if self.right:
              self.right.search(data)
            else:
                print("node not found")
    def delete(self,data):
        if self.val is None:
            print("no node is found")
            return
        if data<self.val:
            if self.left:
                self.left=self.left.delete(data)
            else:
                print("not found")
        elif data> self.val:
            if self.right:
                self.right=self.right.delete(data)
            else:
                print("not found")
        else:
            if self.left is None:
                temp=self.right
                self=None
                return temp
            if self.right is None:
                temp=self.left
                self = None
                return temp
            node=self.right
            while node.left:
                node=node.left
            self.val=node.val
            self.right=self.right.delete(node.val)
        return self
def inorder(Node):
    if Node:
        inorder(Node.left)
        print(Node.val, end=" ")
        inorder(Node.right)
def preorder(Node):
    if Node:
        print(Node.val,end=" ")
        preorder(Node.left)
        preorder(Node.right)

root=Bst(10)
l=[6,3,1,6,98,3,7]
for i in l:
    root.insert(i)
print("\n")
inorder(root)
print("\n")
root.search(3)
print("\n")
preorder(root)
print("\n")
root.delete(10)
print("after deleting\n")
preorder(root)
print("\n")
inorder(root)
