'''
Created on Aug 8, 2020

@author: Q

start from both end l, r
move inward the short one till a longer one is found, the new area is compared to the old one.
if moving the long one, the new area won't be larger.
if l==r, then move both end inward till longer ends are found
'''

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1        
        max_area, current_area = 0, 0
        while (i<j):            
            l = height[i]
            r = height[j]
            #print (l,r)
            current_area = (j-i) * min(l, r)
            #print(current_area)
            if current_area > max_area:
                max_area = current_area 
            if l <= r: # left end is lower, equal deals with same l and r               
                while (i<j):                    
                    i=i+1
                    if height[i]>l:
                        break
            if l >= r: # right end is lower, equal deals with same l and r
                while (i<j):                    
                    j=j-1
                    if height[j]>r:
                        break
        return max_area

a = [1,8,6,2,5,4,8,3,7]
msol = Solution()
print(msol.maxArea(a))