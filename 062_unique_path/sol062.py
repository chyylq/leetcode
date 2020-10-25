'''
Created on Oct 24, 2020

@author: Q
'''
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        total_steps = (m-1) + (n-1)        
        ret = 1        
        for i in range(m-1):
            ret = ret * (total_steps-i)            
        for i in range(m-1):
            ret = ret / (1+i)
        return ret
    
sol = Solution()
m = 7
n = 3
print(sol.uniquePaths(m,n))
