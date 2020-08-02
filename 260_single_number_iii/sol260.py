'''
Created on Aug 2, 2020

@author: Q

use XOR to get the 2 unique single num's XOR
then divide original list into 2 groups based on same bit showing either 1 or 0 in the XOR results
use XOR in the 2 lists to get the final results
'''
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = 0
        for x in nums:
            ret = x ^ ret
        max_bit = int.bit_length(ret)        
        i = 0
        while i < max_bit:
            if ((ret>>i) & 1) == 1: break
            i += 1
        # i is the lowest bit that different in 2 numbers
        l1 = []
        l2 = []
        for x in nums:
            if ((ret ^ x)>>i & 1) == 1:
                l1.append(x)
            else:
                l2.append(x)
        ret1, ret2 = 0, 0
        for x1 in l1:
            ret1 = x1 ^ ret1
        for x2 in l2:
            ret2 = x2 ^ ret2
        
        return (ret1, ret2)
    
m = Solution()
a = [1,2,1,3,2,5]
res = m.singleNumber(a)
print (res)  
        
                
        