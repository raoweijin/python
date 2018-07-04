"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val= None):
        self.val = val
        self.left, self.right = None, None



class Solution:
    """
    @param: root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """

    def createTree(self):
        root = TreeNode(1);
        root.left = TreeNode(2);
        root.right = TreeNode(3)
        root.left.left = TreeNode(4);
        root.left.right = TreeNode(5);
        return root;
        
    def intern(self, root):
        # write your code here
        if(root == None):
            return [];
        
        
        left = self.intern(root.left)
        
        right = self.intern(root.right)

        res = []
        res.append(root.val)
        res= res + left+right;
        return res
            
    def preorderTraversal(self, root):
   
        return self.intern(root);
     

    def maxDepth(self, root):  
        
        return self.help2(root,0);
        
    def help2(self,root,level):
        if(root == None):
            return level
        if(None != root):
            level +=1;

        left = self.help2(root.left,level)
            
 
        right = self.help2(root.right,level)
        return max(left,right)
            
        
        
        
mysolution  = Solution()
treeRoot = mysolution.createTree();
print(mysolution.preorderTraversal(treeRoot))    
print( mysolution.maxDepth(treeRoot))   
  