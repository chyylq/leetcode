'''
Created on Jan 30, 2021

@author: Q
'''
class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dis = len(words)+1
        prv, prv_idx = None, -1
        for i in range(len(words)):
            cur = words[i]
            if cur in (word1, word2):
                if not prv:
                    prv = 1 if cur==word1 else 2
                    prv_idx = i                                                                                              
                else:
                    if (prv==1 and cur==word2) or (prv==2 and cur==word1):
                        dis = min([dis, i-prv_idx])
                        prv = 1 if cur==word1 else 2
                        prv_idx = i
                    elif (prv==1 and cur==word1) or (prv==2 and cur==word2):
                        prv_idx = i
                
        return dis
    

msol = Solution()
words = ["practice", "makes", "perfect", "coding", "makes"]
word1 = "makes"
word2 = "makes"
ares = msol.shortestWordDistance(words, word1, word2)
print(ares) 