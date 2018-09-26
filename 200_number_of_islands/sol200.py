'''
Created on Sep 23, 2018

@author: Q

DFS m
'''
class Solution:
    def dfs(self, i, j, grid, M, N):
        for ki,kj in ((-1,0),(0,1),(1,0),(0,-1)):            
            if (i+ki)>=0 and (i+ki)<M and (j+kj)>=0 and (j+kj)<N and grid[i+ki][j+kj] == '1':
                grid[i+ki][j+kj] = '0'                
                #print(grid)                
                self.dfs(i+ki, j+kj, grid, M, N)
        return                
    
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        M = len(grid)
        if M==0: return 0
        N = len(grid[0])
        num_islands = 1
        # build the candidate set
        for i in range(M):
            for j in range(N):
                if grid[i][j]=='1':
                    num_islands += 1
                    self.dfs(i,j,grid,M,N)
        return num_islands-1
    
    
m = Solution()
s = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
print(m.numIslands(s))    
            