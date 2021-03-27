'''
Created on Mar 27, 2021

@author: Q
'''
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prv = 0
        for x in sorted(nums):
            if x==prv:
                return x
            else:
                prv=x
        