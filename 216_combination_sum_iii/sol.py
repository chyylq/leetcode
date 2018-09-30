# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 10:48:40 2018

@author: yilin
"""

class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        def backtrack(cand, curidx, cursum, target, q, result):
            #print (q)
            #print (cursum)
            #print (cand)
            if len(q) >= k:
                return
            for i in range(curidx, len(cand)):
                if (cand[i]+cursum == target) and (len(q)+1 == k):
                    q.append(cand[i])
                    result.append(q.copy())
                    q.pop()
                    return
                elif (cand[i]+cursum < target) and (i < (len(cand)-1)):
                    q.append(cand[i])                  
                    backtrack(cand, i+1, cand[i]+cursum, target, q, result)
                    q.pop()
                else:
                    return
        
        res = []
        backtrack(list(range(1,10)), 0, 0, n, [], res)
        return res
    
m = Solution()
k = 1
n = 0
print(m.combinationSum3(k, n))