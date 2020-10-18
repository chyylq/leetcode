'''
Created on Oct 17, 2020

@author: Q

double sorted list  
pq H descending
each time move one points, points being a start or end points of a building
and if multiple buildings start/end in the same spot 
- start before end; start: highest building first, end: lowest first 
1. see if this is a new building to be added
    a. if the added height > curh, key point appends h's corresponding l
2. see if there is a building to be removed
    a. if the removed height > curh, key point appends h's corresponding l

'''
import heapq

class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        tombstones = {}
        def heap_remove(heap, value):
            tombstones[value] = tombstones.get(value, 0) + 1
            while len(heap) and heap[0] in tombstones and tombstones[heap[0]]:
                tombstones[heap[0]] -= 1
                heapq.heappop(heap)
        
        points = []
        for l,r,h in buildings:
            points.append((l, h, 0)) # start of a building
            points.append((r, -h, 1)) # end of a building
        points.sort(key=lambda x: (x[0], -x[1]))
        res = []
        pq = [0] #pq is min heap, so height is negative
        for point in points:
            if point[2]==0:                
                if point[1]>-pq[0]:
                    res.append([point[0],point[1]])
                heapq.heappush(pq, -point[1])                
            elif point[2]==1:
                #pq.remove(point[1])
                heap_remove(pq, point[1])
                heapq.heapify(pq)
                if -point[1]>-pq[0]:
                    res.append([point[0],-pq[0]])
        return res
                    
    def getSkyline2(self, buildings):
        points = []
        for l,r,h in buildings:
            points.append([l, h, 'start'])
            points.append([r, -h, 'end'])
        points.sort(key=lambda x:( x[0], -x[1]))
        # start before end; start: lowest first, end: highest first
        res, max_heap= [], [0]
        for point in points:
            if point[2] == 'start':
                if point[1]>-max_heap[0]:
                    res.append([point[0],point[1]])
                heapq.heappush(max_heap, -point[1])
            elif point[2] == 'end':  #point[1] is negative number
                max_heap.remove(point[1])
                heapq.heapify(max_heap)
                if -point[1]>-max_heap[0]: #both negative number
                    res.append([point[0],-max_heap[0]])
        return res            
            
m = Solution()
candidates = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
print(m.getSkyline(candidates))
print(m.getSkyline2(candidates))
                