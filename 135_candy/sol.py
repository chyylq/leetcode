# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 18:20:21 2017

@author: yilinqin
"""

class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        cnt = len(ratings)
        if cnt==0: 
            return 0
        left = [1]*cnt
        right = [1]*cnt
        
        for i in range(1,cnt,1):
            if ratings[i]>ratings[i-1]:
                left[i]=left[i-1]+1
                
        for i in range(cnt-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                right[i]=right[i+1]+1
        
        candies = 0
        for i in range(cnt):
            candies = candies+max(left[i],right[i])
        
        return candies

m = Solution()
a = [1,3,2,2,2,1]
print (m.candy(a))