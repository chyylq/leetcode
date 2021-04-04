'''
Created on Apr 4, 2021

@author: Q
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        res, q, temp, flag = [],[root],[],1        
        while q:
            for i in range(len(q)):
                node = q.pop(0)
                temp += [node.val]
                if node.left: q+=[node.left]
                if node.right: q+=[node.right]
            res+=[temp[::flag]]
            temp = []
            flag*=-1
        return res
        