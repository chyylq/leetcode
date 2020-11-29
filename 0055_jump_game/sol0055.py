'''
Created on Nov 29, 2020

@author: Q

BFS
'''

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def func(numbers, n, vis, cand):
            next_cand = []
            print(cand)
            for pos in cand:
                for i in range(0, numbers[pos]+1):
                    next_pos = pos+i
                    if next_pos >= n:
                        return True
                    elif vis[next_pos] == 0:
                        vis[next_pos]=1
                        next_cand.append(next_pos)
            if len(next_cand)==0: 
                return False
            return func(numbers, n, vis, next_cand)
                    
        N = len(nums)
        visited = [0]*N
        candidate = [0]               
        return func(nums, N-1, visited, candidate)
    
    def canJump2(self, nums):
        last_pos = len(nums)-1
        for i in range(last_pos, -1, -1):            
            if nums[i]+i>=last_pos:
                last_pos=i
        return last_pos==0
            
        
m = Solution()            
nums = [2,3,1,1,4]#[3,2,1,0,4] # #
print(m.canJump2(nums))  
        
            
            
        
