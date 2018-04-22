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
# from solution section
# https://discuss.leetcode.com/topic/28095/68-ms-fast-python-solution-beat-97-only-put-starting-index-in-stack-detailed-explaination/9
# fast
# lst(last) is -1 or the starting index of the unbroken bracket chain we just extended with a matching ')'
# so if we just encounter a '(' , we didn't extend the unbroken bracket chain, so we need to set lst as -1 no matter lst was -1 or not.
class Solution2(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        result=0
        stk=[]
        lst=-1
        for i in xrange(len(s)):            
            if s[i]=='(':
                if lst!=-1:
                    stk.append(lst)
                    lst=-1
                else:
                    stk.append(i)
            else:
                if stk:
                    stt=stk.pop()
                    if i-stt+1>result:
                        result=i-stt+1
                    lst=stt
                else:
                    lst=-1
            print s[i], stk, lst, result
        return result
        
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
        
class Solution3:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        l = []        
        q = [] # (start, end)
        # first pass         
        for i in range(len(s)):            
            if s[i]=='(':
                l.append(i)
            elif s[i]==')':                                    
                if len(l)>0:
                    k = l.pop()
                    while (len(q)>0 and q[-1][1]>k):
                        q.pop()
                    q.append((k,i))                                        
        # second pass to count only consecutive matched pairs
        print(q)
        cur_len = 0
        prv_idx = -1
        for j in range(len(q)):
            if prv_idx == (q[j][0]-1):
                cur_len = cur_len + q[j][1]-q[j][0]+1
            else:
                cur_len = q[j][1]-q[j][0]+1
            prv_idx = q[j][1]                
            if cur_len > max_len:
                max_len = cur_len
        return max_len
		
a = '((()()())((())'

msol = Solution2()
print msol.longestValidParentheses(a)