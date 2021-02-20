"""
Created on Sat Feb 20 12:42:11 2021

@author: yilin

use scanline
(entry, exit) ->  ( (entry, +1), (exit, -1))
overlap = 0
from the queue, if overlap decreases to 0, this is a start point, elif overlap increases to 1, this is an end point
"""


# Definition for an Interval.
class Interval(object):
    def __init__(self, start=None, end=None):
        self.start = start
        self.end = end


class Solution(object):
    def employeeFreeTime(self, schedule):
        """
        :type schedule: [[Interval]]
        :rtype: [Interval]
        """
        queue = list()
        for employee in schedule:
            for interval in employee:
                #queue.append((interval.start, 1))
                #queue.append((interval.end, -1))
                queue.append((interval[0], 1))
                queue.append((interval[1], -1))
        queue = sorted(queue)
        print(queue)
        overlap, freetime, cur_start = 0, list(), 0        
        for pt in queue:
            overlap += pt[1]            
            if overlap==0:  # currently free, find the end point
                cur_start = pt[0]                    
            elif overlap>0 and cur_start>0: # currently not free, record the start point
                #freetime.append(Interval(cur_start, pt[0]))
                freetime.append((cur_start, pt[0]))
                cur_start = -1           
                      
        return freetime
    
    
msol = Solution()
sch = [[[7,24],[29,33],[45,57],[66,69],[94,99]],[[6,24],[43,49],[56,59],[61,75],[80,81]],[[5,16],[18,26],[33,36],[39,57],[65,74]],[[9,16],[27,35],[40,55],[68,71],[78,81]],[[0,25],[29,31],[40,47],[57,87],[91,94]]]
ares = msol.employeeFreeTime(sch)
print(ares) 
        