"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):
        res = self.helper(root)
        if res == -1:
            return False
        else:
            return True
        
    def helper(self,root):
        if root ==None:
            return 0
        # write your code here
        left = self.helper(root.left)
        right = self.helper(root.right)
        if left == -1 or right== -1:
            return -1
        if abs(left-right) < 2:
           return -1
        return max(left,right)+1