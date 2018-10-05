'''
Created on Sep 30, 2018

@author: Q
'''
class Solution:
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # index: number; dp[i]: how many addition paths sum to the number
        l = [0]*(target+1)
        for k in nums:
            if k <= target:
                l[k] = 1
             
        def dp(num):
            if num>target:
                return            
            for k in nums:
                if num+k <= target:
                    l[num+k] = l[num+k]+l[num]
            dp(num+1)
                
        dp(0)
        return l[target]
                     
            
m = Solution()
nums = [9]
target = 3
print(m.combinationSum4(nums, target))       
