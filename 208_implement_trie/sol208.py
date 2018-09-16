'''
Created on Sep 13, 2018

@author: Q
'''

class TrieNode:
    def __init__(self):
        self.val = ''
        self.next = dict() # for fast check {key in the node: node}
        
        
class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """                 
        self.root = TrieNode()
    
    def find(self, word):
        """
        iteratively find starting from the root
        return the node shaing the same prefix but not the suffix
        and the remaning word after the common prefix
        """
        if word[0] in self.root.next.keys():
            curnode = self.root.next[word[0]]
            if len(word)>1:
                curword = word[1:] 
                for i in range(len(word)-1):
                    if curword[0] in curnode.next.keys():
                        curnode = curnode.next[curword[0]]
                        curword = curword[1:] if len(curword)>1 else ''
                    else:
                        break
            else:
                curword = ''
        else:
            curnode = self.root
            curword = word
        return curnode, curword
                    
            
    def add(self, node, word):
        """
        add the current word to the child of the node
        """
        curnode = node
        for i in range(len(word)):
            childnode = TrieNode()
            childnode.val = word[i]
            curnode.next[word[i]] = childnode
            curnode = childnode
        curnode.next[''] = ''   

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node, word_left = self.find(word)
        if word_left != '':
            self.add(node, word_left)
        else:
            node.next[''] = ''
            
            
    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node, word_left = self.find(word)
        if (word_left=='') and ('' in node.next.keys()):
            return True
        else:
            return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node, word_left = self.find(prefix)
        if word_left == '':
            return True
        else:
            return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
            
            
trie = Trie()
print (trie.root.val)

#trie.insert("apple")
print(trie.startsWith("app"))
print(trie.find("apple"))
print(trie.search("app"))
print(trie.startsWith("app"))
print(trie.insert("app") )  
print(trie.search("app") )
