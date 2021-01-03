'''
Created on Jan 3, 2021

@author: Q

'''
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []                
        for i,j in sorted(intervals):            
            if len(res)>0 and res[-1][1] >= i:
                res[-1][1] = max(res[-1][1], j)
            else:
                res.append([i,j])
        return res
            

msol = Solution()
intervals = [[1,4],[4,5]]
ares = msol.merge(intervals)
print(ares)                