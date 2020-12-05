'''
Created on Dec 5, 2020

@author: Q
'''
from collections import Counter
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, K):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        ctr = Counter()
        l, res = 0, 0
        for r in range(len(s)):
            ctr[s[r]] = ctr[s[r]]+1            
            if len(ctr)<=K:
                res = max(res, r-l+1)                 
            else:
                for k in range(l, r, 1):
                    ctr[s[k]] = ctr[s[k]] - 1
                    if ctr[s[k]] == 0:
                        del ctr[s[k]]
                    if len(ctr)<=K:
                        l = k+1                        
                        break                                
                res = max(res, r-l+1)
        return res

msol = Solution()
a = "aa" #"dvdf" #"abcabcbb"
k1 = 1
ares = msol.lengthOfLongestSubstringKDistinct(a, k1)
print(ares)