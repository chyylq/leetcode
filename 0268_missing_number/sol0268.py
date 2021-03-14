'''
Created on Mar 13, 2021

@author: Q
'''
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = len(nums)
        for i,x in enumerate(nums):
            res ^= i^x
        return res
    
