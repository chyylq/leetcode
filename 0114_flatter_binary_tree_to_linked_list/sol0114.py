'''
Created on Jan 31, 2021

@author: Q
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def do_flatter(self, root):
        if root.left is None and root.right is None:
            return root
        left_end, right_end = None, None
        if root.left:
            left_end = self.do_flatter(root.left)
        if root.right:
            right_end = self.do_flatter(root.right)
        if left_end:
            left_end.right = root.right
        root.right = root.left
        root.left = None
        return right_end
            
    
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if root is None: return None
        self.do_flatter(root)
        return root
    
