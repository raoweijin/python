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
            
        
class Solution2:
    """
    @param root: The root of binary tree.
    @return: Preorder in list which contains node values.
    """
    def preorderTraversal(self, root):
        res = []
        stack = []
        if (root != None):
            stack.append(root)
        while stack != []: 
            root = stack.pop()        
            res.append(root.val)
            if root.right != None:
                stack.append(root.right)
            if root.left != None:
                stack.append(root.left)
            
        return res 
        
    def inorderTraversal(self, root):
        res = []
        stack = []
        if (root != None):
            stack.append(root)
        while stack != []: 
            if(root != None):
                print("root is ",root.val)
            while root != None and root.left != None:
                stack.append(root.left)
                root= root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right
            if(root != None):
                stack.append(root)            
        return res   


    def postorderTraversal(self, root):
        result = []
        stack = []
        prev = None
        cur = root
 
        if (root == None):
            return result;    

        stack.append(root);
        while (stack!= []):
            curr = stack[-1];
            if (prev == None or prev.left == curr or prev.right == curr):  # traverse down the tree
                if (curr.left != None):
                    stack.append(curr.left);
                elif (curr.right != None):
                    stack.append(curr.right);
                
            elif (curr.left == prev):  # traverse up the tree from the left
                if (curr.right != None): 
                    stack.append(curr.right);
                
            else : #traverse up the tree from the right
                result.append(curr.val);
                stack.pop();
            
            prev = curr;
        

        return result;
        
         
mysolution  = Solution()
treeRoot = mysolution.createTree();
preOrder = Solution2()
res = preOrder.preorderTraversal(treeRoot)

print("res is ",res)

res = preOrder.inorderTraversal(treeRoot)

print("res of inorder is ",res)

res = preOrder.postorderTraversal(treeRoot)

print("res of postorder is ",res)