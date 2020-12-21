'''
Created on Dec 21, 2020

@author: Q
'''

class Solution(object):
    def maxCoins_memoization(self, nums):
        N = len(nums)
        dp = [[0 for _  in range(N)] for _ in range(N)]
        def take_one_out(i, j):
            if dp[i][j]:
                return dp[i][j]
                        
            for k in range(i,j+1):
                x1,x2=1,1
                y1,y2=0,0
                if i>0:
                    x1=nums[i-1]
                if j<N-1:
                    x2=nums[j+1]
                if k-1>=i:
                    y1=take_one_out(i,k-1)
                if k+1<=j:
                    y2=take_one_out(k+1,j)
                dp[i][j] = max(dp[i][j], x1*nums[k]*x2 + y1 + y2)
            return dp[i][j]
        
        take_one_out(0, N-1)
        print(dp)            
        return dp[0][N-1]     
            
    
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """        
        def take_one_out(nums):
            """
            divide and conquer / dfs
            """
            N = len(nums)
            res = 0
            for i in range(N):
                x1,x2=1,1
                if i>0:
                    x1=nums[i-1]
                if i<N-1:
                    x2=nums[i+1]
                res = max(res, x1*nums[i]*x2 + take_one_out(nums[0:i]+nums[i+1:]))
            return res
        
        #return take_one_out(nums)
    
        # dp
        # dp[i,j] for result between ith and jth in nums
        # dp[i,j] = max( dp[i,k-1] + nums[i-1]*nums[k]*nums[j+1] + dp[k+1,j]), k is the last to take out in between i and j
        # fill the matrix diagonal
        N = len(nums)
        dp = [[0 for _  in range(N)] for _ in range(N)]
        for l in range(0,N):
            i = 0
            j = l
            while (j<N):
                for k in range(i,j+1):
                    x1, x2 = 1, 1
                    y1, y2 = 0, 0
                    if k>0:                        
                        y1 = dp[i][k-1]                        
                    if k<N-1:                        
                        y2 = dp[k+1][j]
                    if i>0:
                        x1 = nums[i-1]
                    if j<N-1:
                        x2 = nums[j+1]
                    #print(i,k,j)
                    dp[i][j] = max(dp[i][j], x1*nums[k]*x2 + y1 + y2)
                i = i+1
                j = j+1
        #print(dp)
        return dp[0][N-1]
    
                

msol = Solution()
nums = [3,1,5,8] 
ares = msol.maxCoins_memoization(nums)
print(ares)      