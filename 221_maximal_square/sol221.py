'''
Created on Nov 15, 2020

@author: Q

Use existing detected square to detect the square in a new spot
let's start from the top left, the current point is the lower right of the square
the current point is [i,j] and is 1, then it is based on the square ended in [i-1,j-1] and the edges along [0:i,j] and [i,0:j] to determine the new square
the new square's edge length is the min of both edges [0:i,j] and [1,0:j] and edge of the square [i-1,j-1]
one step further, the edge along [0:i,j] and [i,0:j] are the edges of the square based on [i-1,j] and [i,j-1], so all three are previous identified squares
we have DP as the edge of the square with its lower right corner at [i,j]
DP[i,j] = min(DP[i-1,j], DP[i,j-1], DP[i-1,j-1]) +1

'''
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        if m==0: return 0
        n = len(matrix[0])
        if n==0: return 0
        dp = [[0 for _ in range(n)] for _ in range(m)]
        max_edge_len = 0
        for j in range(n):
            dp[0][j] = int(matrix[0][j])
            if max_edge_len < dp[0][j]:
                max_edge_len = dp[0][j]
        for i in range(m):
            dp[i][0] = int(matrix[i][0])
            if max_edge_len < dp[i][0]:
                max_edge_len = dp[i][0]
        #print(dp)        
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]=='1':
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
                    if max_edge_len < dp[i][j]:
                        max_edge_len = dp[i][j]
        
        return max_edge_len**2
    

a = [['1','0','1','0','0'],['1','0','1','1','1'],['1','1','1','1','1'],['1','0','0','1','0']]                
m = Solution()
print(m.maximalSquare(a))         