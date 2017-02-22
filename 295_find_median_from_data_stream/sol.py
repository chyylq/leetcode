# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 18:54:43 2017

use a min max heap
max heap to store half smaller elements
min heap to store half bigger elements
insert into the heap that makes both tree elements balanced

min/max heap
current node: k
child node: 2k+1, 2k+2
or 
current node: n
parent node: (n-1)/2

@author: Q
"""
import operator

class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.heap_min = []
        self.heap_max = []
        self.i_min = 0
        self.i_max = 0
        
    def insertBottom(self, l, num, predicate):        
        l.append(num)
        if predicate == operator.lt:
            self.i_min = self.i_min+1
            icur = self.i_min-1
        else:
            self.i_max = self.i_max+1        
            icur = self.i_max -1            
        iprt = (icur-1)/2
        
        while (icur>0 and predicate(l[icur], l[iprt])):
            tmp = l[iprt]
            l[iprt] = l[icur]
            l[icur] = tmp
            icur = iprt
            iprt = (icur-1)/2
     
    def replaceTop(self, l, num, predicate):
        if predicate == operator.lt:            
            iend = self.i_min-1           
        else:            
            iend = self.i_max-1
            
        l[0] = num
        icur = 0
        ileft = 2*icur+1
        iright = 2*icur+2
        while (ileft<=iend):            
            if (ileft==iend):
                if predicate(l[ileft], l[icur]):
                    tmp = l[ileft]
                    l[ileft] = l[icur]
                    l[icur] = tmp
                    icur = ileft
                else:
                    break
            else:                
                if (predicate(l[ileft], l[iright]) or l[ileft]==l[iright]) and predicate(l[ileft], l[icur]):                                                         
                    tmp = l[ileft]
                    l[ileft] = l[icur]
                    l[icur] = tmp
                    icur = ileft                    
                elif (predicate(l[iright], l[ileft]) or l[ileft]==l[iright]) and predicate(l[iright], l[icur]):                
                    tmp = l[iright]
                    l[iright] = l[icur]
                    l[icur] = tmp
                    icur = iright                 
                else:                      
                    break                
                ileft = 2*icur+1
                iright = 2*icur+2
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if self.i_max == self.i_min:
            if self.i_max == 0 or num < self.heap_min[0]:
                self.insertBottom(self.heap_max, num, operator.gt)
            else:
                tmp = self.heap_min[0]
                self.replaceTop(self.heap_min, num, operator.lt)
                self.insertBottom(self.heap_max, tmp, operator.gt)
        else:
            if num < self.heap_max[0]:
                tmp = self.heap_max[0]
                self.replaceTop(self.heap_max, num, operator.gt)
                self.insertBottom(self.heap_min, tmp, operator.lt)                
            else:
                self.insertBottom(self.heap_min, num, operator.lt)
        

    def findMedian(self):
        """
        :rtype: float
        """        
        #print self.heap_max
        #print self.heap_min        
        if self.i_max == self.i_min:
            return 0.5*(self.heap_max[0]+self.heap_min[0])
        else:
            return 1.0*self.heap_max[0]        


# Your MedianFinder object will be instantiated and called as such:
m = MedianFinder()
x = [78,14,50,20,13,9,25,8,13,37,29,33,55,52,6,17,65,23,74,43,5,29,29,72,7,13,56,21,31,66,69,69,74,12,77,23,10,6,27,63,77,21,40,10,19,59,35,40,44,4,15,29,63,27,46,56,0,60,72,35,54,50,14,29,62,24,18,79,16,19,8,77,10,21,66,42,76,14,58,20,0]
print len(x)
for i in x:    
    m.addNum(i)

print m.findMedian()