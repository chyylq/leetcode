'''
Created on Oct 7, 2018
1. sort inputs based on start
2. for each new interval, if the start is between the previous start and end then meeting room+1
   since start is sorted, the new interval's start is no earlier than the previous ones, so just need to check if the new start < previous end
   we can also discard all previous intervals if their end is < new start, because all future intervals won't overlap
   to store previous intervals, we just need to store its end points and maintain its order for binary search purpose  
@author: Q
'''

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

import bisect

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """        
        s_intervals = sorted(intervals, key=lambda x:x[0])#x.start)
        min_rooms = 0
        #maintain the candidates that may have conflicts, end time is enough b/c the input is based on start time
        q_overlap = []  
        for interval in s_intervals:
            idx = bisect.bisect(q_overlap, interval[0])#.start) # binary search            
            q_overlap = q_overlap[idx:]  #discard
            if len(q_overlap)+1 > min_rooms:
                min_rooms = len(q_overlap)+1
            bisect.insort(q_overlap, interval[1])#.end) # insert and keep the sort                           
        return min_rooms
        
m = Solution()
intervals = [[7,10],[2,4]]
print(m.minMeetingRooms(intervals))                
            
            
            