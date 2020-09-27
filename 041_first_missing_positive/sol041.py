'''
Created on Sep 27, 2020

@author: Q

Use the array itself, one spot is for an integer
Move the element into the new spot where its value is the same as index
If negative, ignore, elif greater than the array size, ignore
The 1st missing spot in the newly formed array is the smallest missing integer
'''
import sys

class Solution(object):    
    
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_num = sys.maxsize
        max_num = 0
        for n in nums:
            if n>0 and n<min_num:
                min_num=n
            if n>max_num:
                max_num=n
        if (min_num>1) or (max_num==0):
            return 1
        for i in range(len(nums)):
            val = nums[i]
            if val>=1 and val<=len(nums) and val==nums[val-1]:
                if val-1 != i:
                    nums[i] = 0
                continue
            nums[i] = 0
            while val>=1 and val<=len(nums):
                if nums[val-1] != val:
                    new_val = nums[val-1]
                    nums[val-1] = val  # the target spot set
                    val = new_val # the value from original target                    
                else:
                    break
        print(nums)
        i = 1
        while i<=len(nums):
            if nums[i-1]==0:
                break
            else:
                i=i+1
        return i


n = [3,4,-1,1]
msol = Solution()
print(msol.firstMissingPositive(n))
                