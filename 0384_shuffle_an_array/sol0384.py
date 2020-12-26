'''
Created on Dec 26, 2020

@author: Q
'''
import random
import copy

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.orig_nums = nums
        self.nums = copy.deepcopy(nums)

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.nums = copy.deepcopy(self.orig_nums)
        return self.nums
        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        N = len(self.nums)
        for i in range(N):
            j = random.randrange(N-i)
            self.nums[j], self.nums[N-i-1] = self.nums[N-i-1], self.nums[j]
        return self.nums 


# Your Solution object will be instantiated and called as such:
nums = [1,2,3,4,5,6]
obj = Solution(nums)
print(obj.reset())
print(obj.shuffle())
print(obj.shuffle())
print(obj.shuffle())
print(obj.shuffle())
print(obj.reset())