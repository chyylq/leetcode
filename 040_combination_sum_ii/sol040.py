'''
Created on Sep 29, 2018

@author: Q
'''
class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def backtrack(cand, curidx, cursum, target, q, result):
            #print (q)
            #print (cursum)
            #print (cand)
            for i in range(curidx, len(cand)):
                if i > curidx and cand[i-1]==cand[i]: # if in the same loop previous element same as current, this path has been visited in the previous chain
                    continue 
                elif cand[i]+cursum == target:
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
        backtrack(sorted(candidates), 0, 0, target, [], res)
        return res
    
m = Solution()
candidates = [10,1,2,7,6,1,5]
target = 8
print(m.combinationSum2(candidates, target))