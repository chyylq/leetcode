'''
Created on Sep 13, 2018

@author: Q
'''
from adodbapi.test.adodbapitestconfig import node

class TrieNode:
    def _init__(self):
        self.val = ''
        self.next = dict() # for fast check {key in the node: node}
        
class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """                 
        self.root = TrieNode()
    
    def find(self, node, word):
        if len(word)==1:
            return node
        elif len(word)>1:
            if word[1] in node.next.keys():
                self.find(node[1:], node.next[word[1]])
            
                

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        
        if len(word>0):            
            curnode = self.node
            find(curnode, word)
            
            
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)