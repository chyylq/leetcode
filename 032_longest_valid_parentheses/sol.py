# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 18:16:16 2017

use a stack to match ()
1. '(' push, if seeing ')' pop then check the below array
use an array to record the max len that ends in the current position
2.1. if '()' are neighbors, just check the left and +1
2.2. if '(  )', first check the left of ')' for inner nesting and +1
              then check the left of '(' same as 2.1

@author: yilinqin
"""

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        lmaxlen = [0]*(len(s)+1)
        lstack = []
        
        for idx in range(len(s)):
            if s[idx] == '(':
                lstack.append(idx)
            elif s[idx] == ')':
                if len(lstack)>0:
                    ileft =  lstack.pop()
                    if idx-ileft == 1:
                        lmaxlen[ileft+1] = lmaxlen[ileft]+1
                        lmaxlen[idx+1] = lmaxlen[ileft]+1
                    else:
                        lmaxlen[ileft+1] = lmaxlen[idx]+1
                        lmaxlen[idx+1] = lmaxlen[idx]+1
                        
                        lmaxlen[ileft+1] = lmaxlen[ileft]+lmaxlen[ileft+1]
                        lmaxlen[idx+1] = lmaxlen[ileft]+lmaxlen[idx+1]
        print lmaxlen
        return 2*max(lmaxlen) if len(s)>0 else 0
        

a = '(()())'

msol = Solution()
print msol.longestValidParentheses(a)