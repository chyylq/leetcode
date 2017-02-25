# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 19:11:11 2017

@author: yilinqin
"""

class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        nrow = len(heightMap)
        ncol = len(heightMap[0])
        leftbar = [[] for i in range(nrow)]
        rightbar = [[] for i in range(nrow)]
        upbar = [[] for i in range(nrow)]
        bottombar = [[] for i in range(nrow)]

        for i in range(nrow):
            for j in range(ncol):
                leftbar[i].append(0)
                rightbar[i].append(0)
                upbar[i].append(0)
                bottombar[i].append(0)

        for i in range(nrow):
            imax1 = -1
            imax2 = -1
            for j in range(ncol):                
                if heightMap[i][j] > imax1:
                    imax1 = heightMap[i][j]
                leftbar[i][j] = imax1
                if heightMap[i][ncol-1-j] > imax2:
                    imax2 = heightMap[i][ncol-1-j]
                rightbar[i][ncol-1-j] = imax2
                    
        for j in range(ncol):
            imax1 = -1
            imax2 = -1
            for i in range(nrow): 
                if heightMap[i][j] > imax1:
                    imax1 = heightMap[i][j]
                upbar[i][j] = imax1
                if heightMap[nrow-1-i][j] > imax2:
                    imax2 = heightMap[nrow-1-i][j]
                bottombar[nrow-1-i][j] = imax2
                
        res = 0
        for i in range(1,nrow-1,1):
            for j in range(1,ncol-1,1):
                h = min(leftbar[i][j],rightbar[i][j],upbar[i][j],bottombar[i][j])
                if heightMap[i][j]<h:                
                    res = res + h - heightMap[i][j]
        
        print leftbar
        print rightbar
        print upbar
        print bottombar
        return res
    

a = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
print a
msol = Solution()
ares = msol.trapRainWater(a)
print ares
                
                