'''
Created on Sep 29, 2018

@author: Q
'''
class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def backtrack(cand, cursum, target, q, result):
            #print (q)
            #print (cursum)
            #print (cand)
            for i in range(len(cand)):
                if cand[i]+cursum == target:
                    q.append(cand[i])
                    result.append(q.copy())
                    q.pop()
                    return
                elif cand[i]+cursum < target:
                    q.append(cand[i])                  
                    backtrack(cand[i:], cand[i]+cursum, target, q, result)
                    q.pop()
                else:
                    return
        
        res = []
        backtrack(sorted(candidates), 0, target, [], res)
        return res
    
m = Solution()
candidates = [2,3,6,7]
target = 7
print(m.combinationSum(candidates, target))