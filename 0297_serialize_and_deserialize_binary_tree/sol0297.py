'''
Created on Feb 14, 2021

@author: Q

serialize to a list the order is BST
it uses a queue for recorded but to be visited nodes from BST
it also puts None in places that are from None parent to keep all nodes reported
the serialization ends when all nodes in the queue are None

deserialize from a list to binary tree
it uses a queue for all leaf nodes from BST order
the deserialization ends when the input list ends

notice we don't need serialize the complete tree, it stops at a node when there is no children
and that is also handled when deserializing as long as the order in transversing the tree is consistent in both processes
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        q = list()
        q.append(root)
        res = ''
        while len(q)>0 and any(x is not None for x in q):
            node = q.pop(0)
            if node is not None:                
                res += str(node.val)
                q.append(node.left)
                q.append(node.right)
            else:
                res += '$'                
            res += '|'      
        return res[:-1]         

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data)==0:
            return None
        data = data.split('|')
        root = TreeNode(data[0])        
        q = [root]        
        data = data[1:]
        while len(data)>0:
            parent = q.pop(0)            
            val_l, val_r = data[0], '$'
            if len(data)>1:
                val_r = data[1]
            if val_l != '$':              
                node_l = TreeNode(val_l)
                parent.left = node_l
                q.append(node_l)
            if val_r != '$':
                node_r = TreeNode(val_r)
                parent.right = node_r
                q.append(node_r)
            data = data[2:]
        return root
                
            
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))