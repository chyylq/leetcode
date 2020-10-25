'''
Created on Oct 24, 2020

@author: Q

DP:
a: number of paths up till [i,j]
a[i,j] = a[i-1,j] + a[i,j-1], a[i,j] is not obstacle 
       = 0, a[i,j] is obstacle
'''
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        a = [[0 for _ in range(n)] for _ in range(m)]
        if obstacleGrid[0][0] == 1: return 0
        a[0][0] = 1
        for i in range(m):
            for j in range(n):
                if (i>0) or (j>0):
                    if obstacleGrid[i][j] != 1:
                        a[i][j] = (a[i-1][j] if i-1>=0 else 0) + (a[i][j-1] if j-1>=0 else 0)
                    else:
                        a[i][j] = 0
        #print (a)
        return a[-1][-1]
    

sol = Solution()
l = [ [0,0,0], [0,1,0], [0,0,0]]
print(sol.uniquePathsWithObstacles(l))