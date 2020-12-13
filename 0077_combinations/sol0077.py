'''
Created on Dec 13, 2020

@author: Q
'''
import copy

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        visited = list()
        
        def form_one_set(n, k, cur_set):
            #cur_set = copy.deepcopy(cur_set_in)
            if len(cur_set)==0:
                start_idx = 1
            else:
                start_idx = max(cur_set)+1
            for i in range(start_idx, n+1, 1):
                cur_set.append(i)
                if len(cur_set)==k:
                    visited.append(copy.deepcopy(cur_set))                    
                else:
                    form_one_set(n, k, cur_set)
                cur_set.pop()
                   
        form_one_set(n, k, [])
        return visited
    
    def combine_dfs(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        visited = list()
        
        def dfs(n, k, cur_set):            
            if len(cur_set)==k:
                visited.append(cur_set)
                return
            
            for i in range(cur_set[-1]+1 if len(cur_set)>0 else 1, n+1, 1):
                dfs(n, k, cur_set+[i])   # note if we do it this way compared to line28 in 1st sol, we don't need line29 top pop in 1st sol
        
        dfs(n, k, [])   
        return visited
    
    
    
msol = Solution()
n = 4
k = 2
ares = msol.combine_dfs(n, k)
print(ares)