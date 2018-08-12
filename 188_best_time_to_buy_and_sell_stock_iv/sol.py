# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 09:11:50 2018

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
        p_a = [[0]*len(prices) for x in range(k+1)]
        p = [[0]*len(prices) for x in range(k+1)]
        for m in range(1,k+1):
            for i in range(len(prices)):
                if i==2*(m-1):
                    p_a[m][i] = p[m-1][i-1]-prices[i]
                elif i>2*(m-1):
                    p_a[m][i] = max(p_a[m][i-1], p[m-1][i-1]-prices[i] )
                if i>=m:
                    p[m][i] = max(p[m][i-1],p_a[m][i]+prices[i])
        #print (p_a)
        #print (p)
        #print (max(p))
        return max([max(x) for x in p])
        
m = Solution()
k=2
prices = [2,4,1]
prices = [2,1,2,0,1]
print (m.maxProfit(k,prices))