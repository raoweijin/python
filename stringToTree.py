'''
Example
Given s = "4(2(3)(1))(6(5))", return the tree root node representing the following tree:

       4
     /   \
    2     6
   / \   / 
  3   1 5   
 '''
 
 """
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param s: a string
    @return: a root of this tree
    """
    def str2tree(self, s):
        # write your code here
        length = len(s)
        if 0 == length:
            return None
        nodeStack = []
        state = "Root"
       
        for ie in s:
            if state == "Root":
                root = TreeNodeode(ie)
                nodeStack.push(ie)
                state = "Left"
            elif state == "Left":
                if isChar(ie):
                    leftNode = TreeNode(ie)
                    nodeStack.push(leftNode)
             
        
    def isChar(self,char)
            if char <='9' and char>='0':
                return True
            else:
                return False;
        
        
