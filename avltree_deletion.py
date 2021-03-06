class Node:
    def __init__(self,val):
        self.val=val
        self.right=None
        self.left=None
        self.height=1
class avltree:
    def height(self,node):
        if node is None:
            return 0
        return node.height
    def balance(self,node):
        if node is None:
            return 0
        return self.height(node.left)-self.height(node.right)
    def minmumvalueNode(self,node):
        if node is None or node.left is None:
            return node
        return self.minmumvalueNode(node.left)
    def rotater(self,node):
        a=node.left
        b=a.right
        a.right=node
        node.left=b
        node.height=1+max(self.height(node.left),self.height(node.right))
        a.height=1+max(self.height(a.left),self.height(a.right))
        return a
    def rotatel(self,node):
        a=node.right
        b=a.left
        a.left=node
        node.right=b
        node.height = 1 + max(self.height(node.left), self.height(node.right))
        a.height = 1 + max(self.height(a.left), self.height(a.right))
        return a
    def insert(self,key,root):
        if root is None:
            return Node(key)
        elif key<=root.val:
            root.left=self.insert(key,root.left)
        elif key>= root.val:
            root.right=self.insert(key,root.right)
        root.height=1+max(self.height(root.left),self.height(root.right))
        balance=self.balance(root)
        if balance>1 and root.left.val>key:
            return self.rotater(root)
        if balance<-1 and root.right.val<key:
            return self.rotatel(root)
        if balance>1 and root.left.val<key:
            root.left=self.rotatel(root.left)
            return self.rotater(root)
        if balance<-1 and root.right.val>key:
            root.right=self.rotater(root.right)
            return self.rotatel(root)
        return root
    def delete(self,val,node):
        if node is None:
            return node
        elif val<node.val:
            node.left=self.delete(val,node.left)
        elif val>node.val:
            node.right=self.delete(val,node.right)
        else:
            if node.left is None:
                temp=node.right
                node=None
                return temp
            elif node.right is None:
                temp=node.left
                node=None
                return temp
            temp=self.minmumvalueNode(node.right)
            node.val=temp.val
            node.right=self.delete(temp.val,node.right)
            balance=self.balance(node)
            if balance>1 and self.balance(node.left)>=0:
                return self.rotater(node)
            if balance<-1 and self.balance(node.right)<=0:
                return self.rotatel(node)
            if balance>1 and self.balance(node.left)<0:
                node.left=self.rotatel(node.left)
                return self.rotater(node)
            if balance<-1 and self.balance(node.right)<0:
                node.right=self.rotater(node.right)
                return self.rotatel(node)
        return node
    def preorder(self,root):
        if root is None:
            return
        print(root.val,end=" ")
        self.preorder(root.left)
        self.preorder(root.right)

tree=avltree()
Root=None
Root=tree.insert(10,Root)
Root=tree.insert(20,Root)
Root=tree.insert(30,Root)
Root=tree.insert(40,Root)
Root=tree.insert(50,Root)
Root=tree.insert(25,Root)
print("preorderd value is: ")
tree.preorder(Root)
tree.delete(20,Root)
print()
tree.preorder(Root)