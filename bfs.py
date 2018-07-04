"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None



class Solution:
    """
    @param: root: A Tree
    @return: Level order a list of lists of integer
    """
    
    def createTree(self):
        root = TreeNode(1);
        root.left = TreeNode(2);
        root.right = TreeNode(3)
        root.left.left = TreeNode(4);
        root.left.right = TreeNode(5);
        return root;
    def levelOrder(self, root):
        # write your code here
        res =[]
        buf=[]
        buf.append(root)
        while len(buf) != 0:
            temp =[]
            temp2=[]
            for ie in buf: 
                temp2.append(ie.val)
                if ie.left != None:
                    temp.append(ie.left)
                if ie.right != None:
                    temp.append(ie.right)                
            res.append(temp2)
            buf = temp
        return res
mySolution = Solution()
myTree = mySolution.createTree()
print(mySolution.levelOrder(myTree))
            