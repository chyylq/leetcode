'''
Created on Jan 3, 2021

@author: Q

1 loop for 3rd element and
2 points in a loop for 2 sum
'''
import sys
class Solution(object):
    def threeSumClosest(self, nums0, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        nums = sorted(nums0)
        low_diff = sys.maxsize
        res = 0
        for i in range(len(nums)-2):            
            lp, rp = i+1, len(nums)-1
            while (lp<rp):
                cur = nums[i] + nums[lp] + nums[rp]
                if abs(target-cur)<low_diff:
                    res = cur
                    low_diff = abs(target-cur)
                if cur>target:
                    rp -= 1
                elif cur<target:
                    lp += 1
                else:
                    return res
        return res

msol = Solution()
nums = [0,2,1,-3]
target = 1
ares = msol.threeSumClosest(nums, target)
print(ares)
 