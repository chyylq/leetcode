'''
Created on Feb 6, 2021

@author: Q
'''
class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """ 
        prv_end = -1
        for (start, end) in sorted(intervals):
            if start>=prv_end:
                prv_end = end
            else:
                return False
        return True


            