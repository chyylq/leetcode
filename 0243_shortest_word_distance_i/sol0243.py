'''
Created on Jan 30, 2021

@author: Q
'''
class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dis = len(words)+1
        prv, prv_idx = '', 0
        for i in range(len(words)):
            if words[i] in (word1, word2):
                if prv=='':
                    prv = words[i]                              
                elif words[i]!=prv:
                    dis = min([dis, i-prv_idx])
                    prv = words[i]
                prv_idx = i
                
        return dis
    

msol = Solution()
words = ["practice", "makes", "perfect", "coding", "makes"]
word1 = "makes"
word2 = "coding"
ares = msol.shortestDistance(words, word1, word2)
print(ares) 