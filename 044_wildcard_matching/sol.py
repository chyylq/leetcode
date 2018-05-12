# -*- coding: utf-8 -*-
"""
Created on Sun May  6 11:57:09 2018

@author: yilin
"""

class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m = len(p)
        n = len(s)
        if m==0:
            if n==0:
                return True 
            else:
                return False
        if n==0:
            if p=='*':
                return True
            else:
                return False
        a = [[0] * (n+1) for _ in range(m+1)]
        # dp: going foward it only matters till the current match pos in p and s
        # a[i][j] 1 for matches in previous strings and p[i]==s[j] else 0
        # =1 if a[i][j-1]==1 & [i]==*  p is * so it can match anything
        # =1 if a[i-1][j]==1 & p[i]==*  p is a * so it represents an empty string
        # =1 if a[i-1][j-1]==1 & (p[i]==s[j] | p[i]==? | p[j]==*)
        # initialization
        a[0][0]=1
        for j in range(1,n+1):
            is_alphabetic=0
            for i in range(1,m+1):
                if a[i-1][j]==1:
                    if p[i-1]=='*':
                        a[i][j]=1
                    if (p[i-1]=='?' or p[i-1]==s[j-1]) and is_alphabetic==0:
                        a[i][j]=1
                        is_alphabetic=1
                if a[i-1][j-1]==1:
                    if p[i-1]=='*':
                        a[i][j]=1
                    if (p[i-1]=='?' or p[i-1]==s[j-1]):
                        a[i][j]=1
                        is_alphabetic=1
                if a[i][j-1]==1:
                    if p[i-1]=='*':
                        a[i][j]=1
                    
        if a[m][n] == 1:
            return True
        else:
            return False

m = Solution()
print(m.isMatch('aa','a'))
print(m.isMatch('adceb','*a*b'))
print(m.isMatch('','*'))
print(m.isMatch('ab','*?*?*'))        
print(m.isMatch('acdcb','a*c?b'))
