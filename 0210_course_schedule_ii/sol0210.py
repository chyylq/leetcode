'''
Created on Jan 10, 2021

@author: Q

visited is used for both tracking the current path (-1) for cycle detection and label the current solution (1)
'''
import collections

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        courses_total, has_pre_courses = set([x for x in range(numCourses)]), set()
        courses = collections.defaultdict(list)
        visited = [False] * numCourses        
        for c1, c2 in prerequisites:            
            courses[c2].append(c1)
            courses_total.add(c1)
            courses_total.add(c2)
            has_pre_courses.add(c1)
        
        schedule = []
        
        def dfs(visited, cur_course):            
            if visited[cur_course]==-1:
                return False
            elif visited[cur_course]==1:
                return True
            else:
                visited[cur_course]=-1
                for c in courses[cur_course]:
                    if not dfs(visited, c):
                        return False 
                visited[cur_course]=1
                schedule.append(cur_course)                
                return True
                 
        #for c in courses_total.difference(has_pre_courses):
        for c in range(numCourses):            
            if not dfs(visited, c):
                return []            
        return schedule[::-1]

msol = Solution()
numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
ares = msol.findOrder(numCourses,prerequisites)
print(ares)   
                            
                
        