# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 10:43:23 2018

@author: yilin
"""

'''
length of the word as key
a list of word as value
so we can do '.' search one at a time
'''
import collections

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        word_dict = collections.defaultdict(list)
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        if not '.' in word:
            v = self.word_dict[len(word)]
            if not word in v:
                v.append(word)

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        word_len = len(word)
        
        if '.' not in word:
            return word in self.word_dict[word_len]
        
        for w in self.word_dict[word_len]:
            success = True
            for index, ch in enumerate(word):
                if ch != w[index] and ch != '.':
                    success = False
                    break    
            if success:
                return True

        return False
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)