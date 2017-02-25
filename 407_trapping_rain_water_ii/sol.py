# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 19:11:11 2017

Starting from the edge and go towards inside
The reserver is bounded by the height of edge
Think this as pull water from the edge to fill the area till hitting all higher bars
Then repeat this again insdie the higher bars

start from the edge
put point into a priority queue sorted by height asc
maintain the current water level starting from 0
for each point not visited and inside the edge from the queue 
  the reserve is waterlvl - height
  add its 4 neighbors to the queue

@author: yilinqin
"""

import heapq

class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        nrow = len(heightMap)
        if nrow==0: return 0
        ncol = len(heightMap[0])
        if ncol==0: return 0
        visitMap = [[0]*ncol for i in range(nrow)]
        #waterMap = [[] for i in range(nrow)]
        pq = []
        
        for i in range(nrow):
            for j in range(ncol):                
                #waterMap[i].append(0)
                if i==0 or i==nrow-1 or j==0 or j==ncol-1:
                    heapq.heappush(pq, (heightMap[i][j],(i,j)))    
                
        waterlv = 0
        res = 0
        mv = ((0,-1),(0,1),(1,0),(-1,0))
        while pq:
            (val, (icur, jcur)) = heapq.heappop(pq)
            if not visitMap[icur][jcur]:                 
                visitMap[icur][jcur]= 1                              
                for (imv, jmv) in mv:
                    inxt = imv+icur
                    jnxt = jmv+jcur
                    if inxt>=0 and inxt<=nrow-1 and jnxt>=0 and jnxt<=ncol-1:
                        heapq.heappush(pq, (heightMap[inxt][jnxt],(inxt,jnxt)))
        
                waterlv = max(waterlv, heightMap[icur][jcur])
                if icur>0 and icur<nrow-1 and jcur>0 and jcur<ncol-1:
                    #waterMap[icur][jcur] = waterlv - heightMap[icur][jcur]
                    res = res + waterlv - heightMap[icur][jcur]                
        #print (waterMap)
        return res
    

a = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
print a
msol = Solution()
ares = msol.trapRainWater(a)
print ares
                
                