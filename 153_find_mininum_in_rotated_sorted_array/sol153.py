'''
Created on Sep 7, 2020

@author: Q

in the main loop, the current array always includes pivot point: ascending pivot ascending
so whether mid is (l+r)//2 or sometimes to be (l+r)//2+1 is not important, because the structure keeps.   
yet at the very end when there are 2 elements e.g. [5,1], we need to terminate
because if we no longer can maintain the structure in the loop anymore if we do one more step
either we will exclude pivot or keep infinite loop due to not be able to move head/tail forward/backward

For those types of questions, check out the cases towards the end and decide different if/else and loop end condition 
'''

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = len(nums)
        if cnt==0: return None
        if nums[0]<nums[cnt-1]: return nums[0]
        l, r = 0, cnt-1
        while (l<r):   
            if l+1==r:
                break         
            mid = (l+r)//2
            #print(l,r,mid)
            if nums[l] > nums[mid]:
                r = mid
            elif nums[l] < nums[mid]:
                l = mid
        return nums[r]
            
a = [3,4,5,1,2]    
msol = Solution()
print(msol.findMin(a))        