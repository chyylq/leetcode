'''
Created on Jan 9, 2021

@author: Q

backtracking

to speed up, it introduce a globe check to see if the node's dependency edges have all be visited,
if it has all been visited and there is no cycle (otherwise the func would have returned), there is no need to check this node in the following backtracking  
'''
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """        
        visited = [0] * numCourses
        checked = [0] * numCourses
        courses = dict()        
        for c1, c2 in prerequisites:
            if c2 in courses:
                courses[c2].append(c1)
            else:
                courses[c2] = [c1]
            if not c1 in courses:
                courses[c1] = []
        
        def dfs_circle(cur_course):
            if visited[cur_course] == 1:
                return True
            if checked[cur_course] == 1:
                return False
            visited[cur_course] = 1
            for next_course in courses[cur_course]:
                if dfs_circle(next_course):
                    return True
            visited[cur_course] = 0
            checked[cur_course] = 1
            
        for c in courses:
            if dfs_circle(c):
                return False
        
        return True
                
msol = Solution()
numCourses = 2 
prerequisites = [[1,0], [0,1]]
ares = msol.canFinish(numCourses,prerequisites)
print(ares)   
                            
            
                 