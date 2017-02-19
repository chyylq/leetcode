# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 11:09:10 2017

@author: yilinqin
"""

def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    l = []
    def permut(nums_in, idx):
        if idx < len(nums_in):
            for i in range(idx, len(nums_in)):
                nums_cur = nums_in[:]
                tmp = nums_cur[idx]
                nums_cur[idx] = nums_cur[i]
                nums_cur[i] = tmp
                permut(nums_cur, idx+1)
        else:
            l.append(nums_in)
    
    permut(nums, 0)
    
    return l
    
    
a = permute([1,2,3,4])
print a