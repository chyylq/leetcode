'''
Created on Mar 2, 2017

@author: Q
'''

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        
        def largestRectangleArea(heights):
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
        
        nrow = len(matrix)
        if nrow == 0: return 0 
        ncol = len(matrix[0])
        if ncol == 0: return 0
        
        maxrect = 0
        prerow = [0]*ncol
        for i in range(nrow):
            curheight = [0]*ncol            
            for j in range(ncol):
                if matrix[i][j] == '1':
                    curheight[j] = 1+ prerow[j]
            arearect = largestRectangleArea(curheight)
            if arearect > maxrect:
                maxrect = arearect
            
            prerow = curheight
        
        return maxrect
    
    
m = Solution()
a = ["10100","10111","11111","10010"]
res = m.maximalRectangle(a)
print (res)