'''
Created on Mar 13, 2021

@author: Q
'''
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """   
        def func(res, cur_end, cur_set, nums):
            if len(cur_end)==0: return res
            next_end, next_set = [], []
            for s, old_set in zip(cur_end, cur_set):                
                for i in range(s, len(nums)):                                                            
                    res.append(old_set+[nums[i]])
                    next_set.append(old_set+ [nums[i]])
                    next_end.append(i+1)
            return func(res, next_end, next_set, nums)
        
        res = [[]]
        return func(res, [0], [[]], nums)
        
        
        
nums=[1,2,3]
msol = Solution()
ares = msol.subsets(nums)
print(ares)              