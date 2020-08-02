'''
Created on Aug 1, 2020

@author: Q

keep track of bits change
if duplicates -> duplicates in bits 3 times -> add count to check each times one bit flips 
'''
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """        
        max_bit = max(map(int.bit_length, nums))
        ret = 0
        for i in range(max_bit+1):  # to include sign bit
            count = 0   # count the sum of 1's in the same bit across all numbers
            for x in nums:
                count += ((x>>i) & 1)  # bit wise to operation on single bit
            ret |= ((count%3) << i)      # move it back and bit wise operation to add each single bit  
        return ret if ret<2**max_bit else ret-2**(max_bit+1)  # if it is great than the max bit allowed positive, it is a negative number 
                        
                    
m = Solution()
a = [-2,-2,1,1,-3,1,-3,-3,-4,-2]
res = m.singleNumber(a)
print (res)                
            