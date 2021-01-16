'''
Created on Jan 16, 2021

@author: Q

One thing to note is that if a valid solution is found:
b...a...., 
let t_i be the total time up to course i and e_i be the stated end time
and a be the smallest end time among the courses in the solution,
then we can always swap a with the first course b 
since the total time up till original b's position is the same 
the new schedule is still valid
in this way, there is always an arranged schedule that is ordered by ascending ending time
thus we start by sort the courses
then we examine each course sequentially to see if it is in the final schedule

top down dp using memoization
dp[courses_checked, total_time] = max number of courses
  
'''
class Solution(object):
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """        
        memo_dp = dict()
        courses = sorted(courses, key=lambda x: x[1])
        N = len(courses)
        
        def dp(n_courses, total_time):
            if n_courses>=N or total_time>=courses[-1][1]:
                return 0
            if (n_courses, total_time) in memo_dp:
                return memo_dp[(n_courses, total_time)]
            
            # we don't choose the current course
            res = dp(n_courses+1, total_time)            
            # or we choose the current course
            if total_time + courses[n_courses][0] <= courses[n_courses][1]:
                res = max(res, 1+dp(n_courses+1, total_time + courses[n_courses][0]))
            
            memo_dp[(n_courses, total_time)] = res
            #print(memo_dp)
            return res
                
        return dp(0,0)

msol = Solution()
courses = [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
ares = msol.scheduleCourse(courses)
print(ares) 