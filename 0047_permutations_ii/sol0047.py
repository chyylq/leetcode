'''
Created on Dec 13, 2020

@author: Q
'''
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = set()
        
        def dfs(nums, cur_set):
            if len(nums)==0:
                if tuple(cur_set) not in res:
                    res.add(tuple(cur_set))
                return
            
            for i in range(len(nums)):
                dfs(nums[0:i]+nums[i+1:], cur_set+[nums[i]])
        
        dfs(nums, [])
        ret = []
        for x in res:
            ret.append(list(x))
        return ret
    
msol = Solution()
nums= [1,2,3]
ares = msol.permuteUnique(nums)
print(ares)
    