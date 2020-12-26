'''
Created on Dec 26, 2020

@author: Q
'''
import random

class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.nums = [0] * len(w)
        self.nums[0] = w[0]
        for i in range(1, len(w)):
            self.nums[i] = self.nums[i-1] + w[i]
        print(self.nums)  

    def pickIndex1(self):
        """
        :rtype: int        
        """        
        x = random.randrange(0, self.nums[-1])
        #print('x='+str(x))
        # use use binary search
        # right the lower bound index 
        l, r = 0, len(self.nums)-1
        mid = int((l+r) / 2)
        while l<r:
            mid = int((l+r) / 2)
            #print('mid='+str(mid))
            if self.nums[mid]>x:
                r = mid-1
            elif self.nums[mid]<x:
                l = mid+1
            else:
                return mid+1
        if x>=self.nums[l]:
            return l+1
        else:
            return l
    
    def pickIndex(self):
        """
        :rtype: int        
        """        
        # both generating x work
        x = self.nums[-1] * random.random()        
        #x = random.randint(1, self.nums[-1])
        # use use binary search
        # right the lower bound index 
        l, r = 0, len(self.nums)     
        while l<r:
            mid = (l+r) // 2
            #print('mid='+str(mid))
            if self.nums[mid]<x:
                l = mid+1
            elif self.nums[mid]==x:
                return mid+1
            else:
                r = mid
        return l
        

# Your Solution object will be instantiated and called as such:
w = [3,14,1,7]
obj = Solution(w)
print(obj.pickIndex())
print(obj.pickIndex())
print(obj.pickIndex())
print(obj.pickIndex())