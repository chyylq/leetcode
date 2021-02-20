# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 12:42:11 2021

@author: yilin

use scanline
(entry, exit) ->  ( (entry, +1), (exit, -1))
overlap = 0
from the queue, if overlap decreases to 0, this is a start point, elif overlap increases to 1, this is an end point
"""

"""
# Definition for an Interval.
class Interval(object):
    def __init__(self, start=None, end=None):
        self.start = start
        self.end = end
"""

class Solution(object):
    def employeeFreeTime(self, schedule):
        """
        :type schedule: [[Interval]]
        :rtype: [Interval]
        """
        queue = list()
        for employee in schedule:
            for interval in employee:
                queue.append((interval.start, 1))
                queue.append((interval.end, -1))
        queue = sorted(queue)
        #print(queue)
        overlap, prv_pt, freetime, cur_start = 0, 0, list(), 0
        if queue[0][0] == 0:
            cur_start = -1
            prv_pt = -1
        for pt in queue:
            if pt[0] != prv_pt:
                if overlap==0 and cur_start>-1:  # currently free, find the end point
                    freetime.append([cur_start, pt[0]])
                    cur_start = -1
                elif overlap>0 and cur_start==-1: # currently not free, record the start point
                    cur_start = pt[0]
            overlap += pt[1]
            prv_pt = pt[0]
        return freetime