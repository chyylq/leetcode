'''
Created on Dec 5, 2020

@author: Q
'''
from collections import Counter

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        col = Counter(nums)
        i = 0
        for k in (0,1,2):
            for _ in range(col[k]):
                nums[i] = k
                i = i+1            
        return nums

msol = Solution()
nums = [1]#[2,0,2,1,1,0]
ares = msol.sortColors(nums)
print(ares)
            