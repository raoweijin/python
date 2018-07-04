
class node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        root  = node(4)
        left =  node(5)
        right = node (2)
        root.left = left
        root.right = right
        left = node(1)
        right = node(3)
        root.left.left = left
        root.left.right = right
        self.root = root
    def printTree(self):
        root = self.root
        print(" ", end=" ")
        print(root.value)
        print(root.left.value, end=" ")
        print(root.right.value)
        print(root.left.left.value, end=" ")
        print(root.left.right.value)
        
    def inOrder(self,curNode):
        if(curNode != None):
            self.inOrder(curNode.left)
            print(curNode.value, end=" ")
            self.inOrder(curNode.right)
        else:
            return
    #def isBSTTree(self):
    def subFunc(self,curNode, minVal,maxVal):
            if(curNode == None):
                return True
            if((curNode.value<minVal) or (curNode.value>maxVal)):
                return False
            a = self.subFunc(curNode.left, minVal,curNode.value)
            b = self.subFunc(curNode.right,curNode.value,maxVal)
            return a and b
    def add(seflt,a,b):
        return a+b
    def bstSwappedNode(self, root):
        if(curNode == None):
                return True
                
                
                
                
a = BST()
a.printTree()
print(a.add(2,3))
print("***********************")
a.inOrder(a.root)
bTree = a.subFunc(a.root,-9,999)    
print(bTree)    
