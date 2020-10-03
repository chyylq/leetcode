'''
Created on Oct 3, 2020

@author: Q

DP:
D(m) is the min coins needed to reach $m 
= min ( D(m-1) + 1
        D(m-2) + 1
        D(m-5) + 1
        ..
       )
'''
import sys
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        d = [0] * (amount+1)
        for i in range(1,len(d)):
            min_d = sys.maxsize
            for k in coins:                
                if i-k>=0:
                    if d[i-k]<min_d:
                        min_d = d[i-k]+1
            d[i] = min_d
        #print (d)
        return d[-1] if (d[-1]>=0) and (d[-1]<sys.maxsize) else -1

n = [1]
amount = 2
msol = Solution()
print(msol.coinChange(n, amount))
                                    
            
        