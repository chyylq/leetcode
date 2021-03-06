'''
Created on Mar 6, 2021

@author: Q
'''
from collections import defaultdict

class TimeMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = defaultdict(list)

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.map[key].append((timestamp, value))        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """        
        arr = self.map[key]
        if len(arr)==0:
            return ''
        if timestamp < arr[0]:
            return ''
        l, r = 0, len(arr)        
        while (l<r):
            mid = (l+r) // 2
            if timestamp==arr[mid][0]:
                return arr[mid][1]
            elif timestamp<arr[mid][0]:   # l ts mid r
                r = mid
            elif arr[mid][0]<timestamp:   # l mid ts r
                l = mid+1
        # terminate index as the immediate right 
        return arr[r-1][1]
            
            
        