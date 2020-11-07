'''
Created on Nov 1, 2020

@author: Q
starting from 2 I know the steps you choose to the last ending tested floor is: 
m, m-1, m-2 .... 1
this makes the total tests in worst scenario same in each range by decreasing the steps for next egg test by 1 with current egg increase test by 1
then within each step range, just move down each turn,
1,1,1,1,1
now from 2 to 3, the next step to end
S be the maximum steps to reach with E eggs and N throws
It includes the maximum steps to reach with E-1 eggs in N-1 throws (if the egg after this throw breaks so we are left with one less eggs and one less throws)
S[e-1, n-1] -- # floors downstairs as egg breaks
plus the maximum steps to reach with E eggs in N-1 throws (if the egg after this throw dosn't break and we are left with one less throws)
S[e, n-1] -- # floors to achieve upstairs as egg contact
plus 1 (for current floor)
1 -- current floor
S[e, n] = S[e-1, n-1] + 1 + S[e, n-1] 
'''
class Solution(object):
    def superEggDrop(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        if (K==1): return N
        if (N==1): return 1
        S = [[0 for _ in range(N)] for _ in range(K+1)]
        for i in range(K+1):
            S[i][0] = 1
        for j in range(N):
            S[0][j] = 0
        for i in range(1, K+1, 1):
            for j in range(1, N, 1):
                S[i][j] = S[i-1][j-1] + 1 + S[i][j-1]
                if S[K][j] >= N:
                    print (S) 
                    return j+1
                    

sol = Solution()
K=2
N=7
print(sol.superEggDrop(K, N))