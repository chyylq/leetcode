# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 18:16:53 2017

@author: yilinqin
"""

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        cnt = len(heights)
        heightq = []
        idxq = []
        maxarea = 0
        i = 0
        while i < cnt:
            if len(heightq)==0 or heightq[-1]<heights[i]:
                # if queue is empty or current > queue, the area grows
                heightq.append(heights[i])
                idxq.append(i)
            elif heightq[-1]>heights[i]:
                # current < queue, update area with height from queue
                while (len(heightq)>0) and (heightq[-1]>heights[i]):
                    h = heightq.pop()
                    istart = idxq.pop()
                    area = (i - istart) * h
                    if area > maxarea:
                        maxarea = area
                # push the current one so the earliest idx and current height is preserved
                heightq.append(heights[i])
                idxq.append(istart)
            i = i + 1
        
        while len(heightq)>0:
            h = heightq.pop()
            istart = idxq.pop()
            area = (i - istart) * h
            if area > maxarea:
                maxarea = area
                        
        return maxarea

m = Solution()
a = [2,1,5,6,2,3]
print m.largestRectangleArea(a)