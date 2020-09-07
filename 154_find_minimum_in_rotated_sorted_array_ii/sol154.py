'''
Created on Sep 7, 2020

@author: Q
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
            print(l,r,mid)
            if nums[l] == nums[mid]:
                l = l+1 
            elif nums[r] == nums[mid]:
                r = r-1
            elif nums[l] > nums[mid]:
                r = mid
            elif nums[l] < nums[mid]:
                l = mid
        return min(nums[l],nums[r])
            
a = [10,1,10,10,10]
msol = Solution()
print(msol.findMin(a))  