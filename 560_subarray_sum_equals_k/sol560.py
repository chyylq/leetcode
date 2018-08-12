'''
Created on Jul 22, 2018

@author: Q
maintain a hashmap for summartion and count so far
presum starting from 0 to i
each time check if presum-k exists previously,  if yes update the total count 
push summation into hashmap and update the count
'''
class Solution(object):        
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """        
        presum = 0
        ret = 0
        d = {0:1}        
        for i in range(len(nums)):
            presum = presum + nums[i]
            if (presum-k) in d:
                ret = ret + d[presum-k]
            if presum in d:
                d[presum] = d[presum]+1
            else:
                d[presum] = 1                    
        return ret
    

a = [0,0,0,0,0,0,0,0,0,0]
b = 0
#a = [1,1,1]
#b = 2
msol = Solution()
max_len = msol.subarraySum(a, b)
print (max_len)