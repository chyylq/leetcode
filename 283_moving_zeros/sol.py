# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 21:58:02 2018

@author: yilin
"""

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums)>0:
            idx_cur = 0
            for i in range(nums):
                if nums[i] != 0:
                    if idx_cur<i:
                        nums[idx_cur] = nums[i]
                    idx_cur = idx_cur + 1
            nums[idx_cur:] = [0]*(len(nums)-idx_cur)