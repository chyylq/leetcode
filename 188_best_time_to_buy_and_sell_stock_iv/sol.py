# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 09:11:50 2018
for illusion: k,i starts from 1
p_a[k][i] is the profit up till last transaction k-1 plus buy the current buy leg till price i  
p[k][i] is the profit with total k 2 leg transactions up till current price i

p_a[k][i] = max( p_a[k][i-1], p[k-1][i-1]-a[i] )
p[k][i] = p_a[k][i] + a[i] 

initial condition:
p_a[k][:] starting at 2*(k-1)+1=2*k-1 because we need at least 2*(k-1) prices to complete the previous k-1 transactions plus 1 buy leg
p[k][:] starting at 2*k because we need at least 2*k prices to complete the k transactions
@author: yilin
"""
class Solution:
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: 
        """
        if len(prices)<2 or k<1:
            return 0
        # a corner case if 2*k is larger than length of prices to cause memory issue
        if len(prices)<2*k:
            res =0;
            for i in range(len(prices)):
                if(i>0) and (prices[i] > prices[i-1]):
                    res += prices[i]-prices[i-1]  
            return res   
    
        p_a = [[0]*len(prices) for x in range(k+1)]
        p = [[0]*len(prices) for x in range(k+1)]
        for m in range(1,k+1):
            for i in range(len(prices)):
                if i==2*(m-1):
                    p_a[m][i] = p[m-1][i-1]-prices[i]
                elif i>2*(m-1):
                    p_a[m][i] = max(p_a[m][i-1], p[m-1][i-1]-prices[i] )
                if i>=2*m-1:
                    p[m][i] = max(p[m][i-1],p_a[m][i]+prices[i])
        '''
        for i in range(1,k+1):            
            print (p_a[i])
        print ('========')
        for i in range(1,k+1):
            print (p[i])
        #print (max(p))
        '''
        return max([max(x) for x in p])
        
m = Solution()
k=11
#prices = [2,4,1]
#prices = [2,1,2,0,1]
prices = [48,12,60,93,97,42,25,64,17,56,85,93,9,48,52,42,58,85,81,84,69,36,1,54,23,15,72,15,11,94]
print (m.maxProfit(k,prices))