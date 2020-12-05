'''
Created on Dec 5, 2020

@author: Q

moving window + counter(dict) to keep track of the char and its count in the window
'''
from collections import Counter
class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        ctr = Counter()
        l, res = 0, 0
        for r in range(len(s)):
            ctr[s[r]] = ctr[s[r]]+1            
            if len(ctr)<=2:
                res = max(res, r-l+1)                 
            else:
                for k in range(l, r, 1):
                    ctr[s[k]] = ctr[s[k]] - 1
                    if ctr[s[k]] == 0:
                        del ctr[s[k]]
                    if len(ctr)<=2:
                        l = k+1                        
                        break                                
                res = max(res, r-l+1)
        return res

msol = Solution()
a = "ccaabbb" #"dvdf" #"abcabcbb"
ares = msol.lengthOfLongestSubstringTwoDistinct(a)
print(ares)
            