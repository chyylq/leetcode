'''
Created on Aug 9, 2020

@author: Q

1. dp - Bellman Ford
l is #edges (waves) from the source to the end node
z is the end node
D[l, z] = min( D[l-1, z],  D[l-1, k] + d[k, z] for k connecting to z

2. dp
it only moves to the right and down, so no need to consider wave(edge) as how the process evolve
D[i, j] = min( D[i-1,j], D[i,j-1]) + d[i,j]
'''
import sys

class Solution(object):
    def minPathSum_BF(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        if m>0:
            n = len(grid[0])
        else: 
            return 0
        V = m*n
        E = (m-1) + (n-1) + 1    
        D = [[sys.maxsize] * V for i in range(E)]
        # init firt row
        D[0][0] = grid[0][0]                 
        for l in range(1,E):
            for i in range(m):
                for j in range(n):
                    k = i*n + j
                    D_up, D_lt = sys.maxsize, sys.maxsize
                    if (l==2):
                        print (l)
                    if (i-1>=0):
                        D_up = D[l-1][(i-1)*n+j] + grid[i][j]                        
                    if (j-1>=0):                        
                        D_lt = D[l-1][i*n+j-1] + grid[i][j]
                    
                    D[l][k] = min([D[l-1][k], D_up, D_lt])
                    
        return D[E-1][V-1]
    
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        r = len(grid)
        if r>0:
            c = len(grid[0])
        else: 
            return 0
                
        D = [[sys.maxsize] * c for _ in range(r)]
        # init first row, col
        D[0][0] = grid[0][0]
        for j in range(1, c):
            D[0][j] = D[0][j-1] + grid[0][j]
        for i in range(1, r):
            D[i][0] = D[i-1][0] + grid[i][0]
        for i in range(1,r):
            for j in range(1,c):
                D[i][j] = min(D[i-1][j], D[i][j-1]) + grid[i][j]
        
        for x in D:
            print(x)        
        return D[r-1][c-1]
                                                        
    
a = [[1,3,1],[1,5,1],[4,2,1]]
msol = Solution()
print(msol.minPathSum(a))
    
                    
                    