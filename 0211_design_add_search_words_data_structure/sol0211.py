'''
Created on Feb 7, 2021

@author: Q

Trie 
'''
class WordDictionary(object):    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = dict()

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.root
        for c in word:
            if c not in node:
                node[c] = dict()
            node = node[c]
        node['$'] = {}
        
    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        node = self.root
        return self.do_search(word, node)
                
    def do_search(self, word, node):
        if len(word)==0: 
            if '$' in node:
                return True
            else:
                return False
        for i in range(len(word)):
            if word[i] in node:
                node = node[word[i]]
            elif word[i]=='.':                
                for ch in node:
                    if self.do_search(word[i+1:], node[ch]):
                        return True
                return False
            else:
                return False        
        return '$' in node
        

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
wordDictionary = WordDictionary()
wordDictionary.addWord("at")
wordDictionary.addWord("and")
wordDictionary.addWord("an")
wordDictionary.addWord("add")
wordDictionary.addWord("bat")
print(wordDictionary.root)
print(wordDictionary.search(".at")) # return False
#print(wordDictionary.search("a.")) # return True
#print(wordDictionary.search("ab")) # return True
#print(wordDictionary.search(".a")) # return True
