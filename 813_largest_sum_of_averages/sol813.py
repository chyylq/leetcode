'''
Created on Nov 27, 2020

@author: Q

The brutal force approach has repeated usage of a block of array[i:j], so to memoization and to DP is natural 
initially if we need k partition, it can be combined from k1 from [i:s] and k2 from [s+1:j] partitions where k1+k2=k for [i,j]
but that means both s and k need to be checked looping each value, that is not a 2-D array and too many loops
to think more carefully, we can get k+1 partition from k and 1 more partition added and the added partition is straight from AVG(s+1,j)
thus we let say DP[i, k] represents the max sum of averages from 0 till i with k partitions

DP[j, k] = max {DP[i, k-1] + AVG(i+1, j)}  for  0 <= i < j (for first part, we know i+1>=k>=1, that is each element is a partition)   
with boundary condition:
DP[i, 1] = AVG[0, i] 
'''
class Solution(object):
    def largestSumOfAverages(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: float
        """
        N = len(A)
        if N==1: return A[0]        
        sums = [0.0]*N     
        sums[0] = A[0]           
        for i in range(1,N):
            sums[i] = sums[i-1]+float(A[i])
        if K==1: return (sums[N-1]/N)
        DP = [[0.0 for _ in range(K+1)] for _ in range(N)]        
        for i in range(N):
            DP[i][1] = sums[i] / float(i+1)        
        for k in range(2,K+1):
            for j in range(N):
                elem = 0
                for i in range(0, j, 1):
                    cur = DP[i][k-1] + float((sums[j]-sums[i])/(j-i))
                    if elem < cur:
                        elem = cur
                DP[j][k] = elem                
        print(DP)
        return DP[N-1][K]

m = Solution()            
A = [4,1,7,5,6,2,3]
K = 4
print(m.largestSumOfAverages(A,K))   
                
        