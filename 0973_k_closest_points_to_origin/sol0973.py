'''
Created on Mar 6, 2021

@author: Q
'''
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        dist = []
        for x,y in points:
            dist.append((x**2+y**2, [x,y]))
        dist = sorted(dist)        
        return [dist[i][1] for i in range(k)]         

    
msol = Solution()
points = [[1,3],[-2,2]]
k=1
ares = msol.kClosest(points, k)
print(ares)     
            