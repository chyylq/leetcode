'''
Created on Apr 4, 2021

@author: Q
'''
class FirstUnique(object):


    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.l_nums = list()
        self.d_nums = dict()
        self.start_idx = 0
        for num in nums:
            self.add(num)
            

    def showFirstUnique(self):
        """
        :rtype: int
        """
        if len(self.l_nums):
            for i in range(self.start_idx, len(self.l_nums)):
                if self.d_nums[self.l_nums[i]]:
                    self.start_idx = i
                    return self.l_nums[i]
            return -1
        else:
            return -1
        

    def add(self, value):
        """
        :type value: int
        :rtype: None
        """
        if not value in self.d_nums:
            self.l_nums.append(value)
            self.d_nums[value] = True
        else:
            self.d_nums[value] = False


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)