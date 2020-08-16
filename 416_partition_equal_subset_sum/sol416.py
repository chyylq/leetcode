'''
Created on Aug 16, 2020

@author: Q

sum or not sum each number one at a time to all total's from previous rounds
natively it is O(n^2) b/c each number is chosen or not
but the total's can have duplicates, so worst case # previous totals is m = max(nums)
the time complexity is O(mn)
'''
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if sum(nums)%2==1:
            return False
        else:
            target = sum(nums)/2
        prv_set = set()        
        cur_set = set()        
        prv_set.add(0)
        for i in nums:            
            for x in prv_set:  
                if (x+i) == target:
                    return True               
                cur_set.add(x + i)
            prv_set = cur_set.copy()
        return False


           
nums = [1, 3, 5]
msol = Solution()
print(msol.canPartition(nums))               