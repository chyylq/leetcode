'''
Created on Dec 1, 2020

@author: Q

moving window + counter(dict) to keep track of the char and its count in the window

'''
from collections import Counter
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l, res = 0, 0
        strset = Counter()
        for i in range(len(s)):            
            strset[s[i]] = strset[s[i]]+1             
            if strset[s[i]]>1: 
                #print(strset)               
                res = max(res, sum(strset.values())-1)               
                for k in range(l,i):
                    strset[s[k]] = strset[s[k]]-1
                    if s[k]==s[i]:
                        l = k+1                        
                        break
        res = max(res, sum(strset.values()))
        return res

msol = Solution()
a = "abcabcbb"#"dvdf" #"abcabcbb"
ares = msol.lengthOfLongestSubstring(a)
print(ares)
            