'''
Created on Nov 8, 2020

@author: Q
'''
import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        hp = nums[0:k]
        heapq.heapify(hp)
        for i in range(k, len(nums), 1):
            if nums[i]>hp[0]:
                heapq.heappop(hp)
                heapq.heappush(hp, nums[i])        
        return hp[0]

m = Solution()
l = [3,2,3,1,2,4,5,5,6]
k=4
print(m.findKthLargest(l, k))