'''
Created on Oct 3, 2020

@author: Q
Memorization
m is the $
d[m] is a set of all distinct combinations for amount to $m
d[m] = set( all d[m-1] appending 1
            all d[m-2] appending 2
            ...
        )  

the set to maintain the unique combination is cumbersome
now the other way around is thinking about coins

d[m] is the # of all distinct combination for amount to $m
d[m] = d[m] + d[m-1]  + d[m-2] ...  
     = d[m] + d[m-k] for k in coins
so you don't have to worry about keeping the set because the order try each value of coin guarantee it is unique combination        
'''
import bisect
class Solution(object):
    def change2(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        d = [set([()]) for _ in range(0, amount+1)]
        for m in range(1, amount+1):
            l = []
            for k in coins:                
                if m-k>=0:
                    # appending the current coin to the existing list of previous amount
                    for s in d[m-k]: 
                        sl = list(s)
                        bisect.insort(sl, k)
                        l.append(tuple(sl))            
            d[m] = set(l)
        # print(d)
        return len(d[-1])   
   
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        d = [0 for _ in range(0, amount+1)]
        d[0] = 1
        for k in coins:            
            for m in range(1, amount+1):
                if m-k>=0:
                    d[m] += d[m-k]
            print(d)
        return d[-1]
    
    
n = [1,2,5]
amount = 4
msol = Solution()
print(msol.change(amount, n))