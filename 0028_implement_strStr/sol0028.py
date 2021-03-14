'''
Created on Mar 14, 2021

@author: Q
'''
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        i = 0
        m, n = len(haystack), len(needle)
        if m==0 and n==0: return 0        
        while i<m:
            if needle==haystack[i:i+n]:
                return i
            i += 1        
        return -1
        