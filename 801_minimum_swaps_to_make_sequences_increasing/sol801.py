'''
Created on Sep 20, 2020

@author: Q

DP 
At each location, it only matters to what the previous location's digit is. So DP is appropriate
If no swap, it is a minimum of previous location's counts from no-swap and swap
If swap, it is 1 + a minimum of previous location's counts from no-swap and swap
And now you have the counts for current no-swap and swap
D[n, 0] = min(D[n-1,0], D[n-1,1]) if sequence remains increasing 
D[n, 1] = min(D[n-1,0], D[n-1,1])+1 if sequence remains increasing
where n is location
0 is no swap, 1 is swap
'''
import sys

class Solution(object):
    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        cnt = len(A)
        D = [[0,0] for _ in range(cnt)]
        D[0][1] = 1
        print(D)
        for i in range(1, cnt):
            D[i][0] = min(D[i-1][0] if A[i-1]<A[i] and B[i-1]<B[i] else sys.maxsize, D[i-1][1] if B[i-1]<A[i] and A[i-1]<B[i] else sys.maxsize)
            D[i][1] = 1 + min(D[i-1][0] if A[i-1]<B[i] and B[i-1]<A[i] else sys.maxsize, D[i-1][1] if B[i-1]<B[i] and A[i-1]<A[i] else sys.maxsize)
            print(D)
        return min(D[-1][0], D[-1][1])

A = [0,3,5,8,9]
B = [2,1,4,6,9] 
msol = Solution()
print(msol.minSwap(A, B))
                
            