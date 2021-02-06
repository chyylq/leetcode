'''
Created on Feb 6, 2021

@author: Q

one dist 3 cases:
len(s)=len(t)-1: s insert 1 char to be t
len(s)=len(t)+1: s delete 1 char to be t
len(s)=len(t):   s replace 1 char to be 
'''
class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m = len(s)
        n = len(t)
        if m==n-1:  #insert 1 char
            for i in range(n):
                if s == t[0:i] + t[i+1:]:
                    return True
            return False
        elif m+1==n: #delete 1 char
            for i in range(m):
                if t == s[0:i] + s[i+1:]:
                    return True
            return False
        elif m==n:
            for i in range(m-1):
                if s[0:i] + s[i+1:] == t[0:i] + t[i+1:]:
                    return True
            return False
        else:
            return False

                
                