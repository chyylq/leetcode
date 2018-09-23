# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 10:57:25 2018

@author: yilin
"""

class Solution:
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        
        return [arr[y[0]] for y in sorted(sorted( [(i,abs(x-z)) for i,z in enumerate(arr)], key=lambda item: item[1])[0:k], key=lambda item: item[0]) ]
    
    
m = Solution()
print (m.findClosestElements([1,2,3,4,5],4,3))