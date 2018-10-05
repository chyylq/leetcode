# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        bleft, bright = None, None        
        if (root.left != None):
            bleft = self.lowestCommonAncestor(root.left, p, q)                    
        if (root.right != None):
            bright = self.lowestCommonAncestor(root.right, p, q)
                                
        if bleft and bright: return root  # check LCA first from both children        
        if (root == p) or (root == q): return root  # then check current node's eligibility 
        if bleft: return bleft # last return child's eligibility
        else: return bright
