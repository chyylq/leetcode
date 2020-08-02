'''
Created on Aug 1, 2020

@author: Q

use xor to cancel out duplicates
'''
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        for i in range(len(nums)):
            ret = nums[i] ^ ret
        return ret

m = Solution()
inp = [4,1,2,1,2]
print(m.singleNumber(inp))