'''
Created on Mar 6, 2021

@author: Q

if   a % k = m
and  b % k = n
then (b-a) % k = 0 

'''
class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """        
        if k==0:
            return any([nums[i]==0 and nums[i+1]==0 for i in range(len(nums)-1)])
        d_mod = dict()  
        d_mod[0] = -1               
        for i in range(len(nums)):
            if i==0:
                total = nums[i]
            else:
                total += nums[i]            
            if k!=0:
                rem = total % k            
                if rem in d_mod and i-d_mod[rem]>1:
                    return True
                elif not rem in d_mod:
                    d_mod[rem] = i            
        return False
    
msol = Solution()
s = [23, 2, 4, 6, 7]
k=6
ares = msol.checkSubarraySum(s, k)
print(ares)     
            
            
            
            
        