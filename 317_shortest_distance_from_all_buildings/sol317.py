'''
Created on Oct 16, 2018

@author: Q

BFS across all houses
then add total distance
'''
import sys
class Solution:
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def BFS(grid, dist, nrow, ncol, q):
            step = 1
            while len(q)>0:
                q_next = []
                for (x,y) in q:
                    for (i,j) in [(-1,0),(1,0),(0,-1),(0,1)]:                        
                        if (x+i)>=0 and (x+i)<nrow and (y+j)>=0 and (y+j)<ncol: # in the grid
                            if grid[x+i][y+j]==0: # pass freely
                                if dist[x+i][y+j]==sys.maxsize: # first visit
                                    dist[x+i][y+j] = step
                                    q_next.append((x+i, y+j))
                                    #print (dist)
                #print(q_next)
                q = q_next
                step += 1                             
        
        seeds = []
        nrow = len(grid)
        if nrow==0: return -1
        ncol = len(grid[0])
        for i in range(nrow):
            for j in range(ncol):
                if grid[i][j]==1:
                    seeds.append((i,j))
        
        num_houses = len(seeds) # houses to start
        if num_houses==0: return -1
        dist = [[[sys.maxsize]*ncol for i in range(nrow)] for j in range(num_houses)] # distance matrix
        
        for k in range(num_houses):
            BFS(grid, dist[k], nrow, ncol, [seeds[k]])
            #print (dist[k])
        
        dist_total = [[0]*ncol for i in range(nrow)]
        for i in range(nrow):
            for j in range(ncol):
                for k in range(num_houses):
                    if dist[k][i][j]==sys.maxsize or dist_total[i][j]==sys.maxsize:
                        dist_total[i][j] = sys.maxsize
                    else:
                        dist_total[i][j] += dist[k][i][j]
        
        #print(dist_total)
        #print (sys.maxsize)
        min_dist = min([item for sublist in dist_total for item in sublist])
        if min_dist>=sys.maxsize:
            return -1
        else:
            return min_dist


m = Solution()
maps = [[1,1,1,1,1,0],[0,0,0,0,0,1],[0,1,1,0,0,1],[1,0,0,1,0,1],[1,0,1,0,0,1],[1,0,0,0,0,1],[0,1,1,1,1,0]]#[[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
print (m.shortestDistance(maps))

