'''
Created on Aug 29, 2020

@author: Q

If one pass, we get p[0,n] as the largest PnL in [0,n] by calculating p[0,1],p[0,2]...p[0,n]
so one pass we get all i's largest PnLs in p[0,i] with one end fixed
For two passes, it is two parts: p[0,i] + p[i+1,n] and notice 0 in the 1st part and n in the 2nd part is fixed
And recall we just need one pass for p[0,i] or p[i+1,n] as long as one end fixed, so we can use memoization to precalculate both parts in p[0,i] + p[i+1,n] O(n)
Then we do another scan to find the maximum of the sum of two segments just moving segment index by 1 each time O(n) 
'''
import sys

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        len_px = len(prices)
        if len_px<=1: return 0
        if len_px==2: return prices[1]-prices[0] if prices[1]-prices[0]>0 else 0
        # 1 pass to calculate p[0,i] and p[i,n]
        p_cur, p1, p2 = [0]*len_px, [0]*len_px, [0]*len_px
        p_max, px_min, px_max = -1, sys.maxsize, -1
        # calculate pnl of min entry and current exit        
        for i in range(len_px):
            if prices[i]<px_min:
                px_min=prices[i]
            p_cur[i] = prices[i] - px_min        
        # cumulatively find the max of pnl till current
        for i in range(len_px):
            if p_cur[i]>p_max:
                p_max = p_cur[i]
            p1[i] = p_max
        # calculate pnl of current entry and max exit
        p_cur, p_max = [0]*len_px, -1
        for i in range(len_px-1,-1,-1):
            if prices[i]>px_max:
                px_max=prices[i]
            p_cur[i] = px_max - prices[i]
        for i in range(len_px-1,-1,-1):
            if p_cur[i]>p_max:
                p_max = p_cur[i]
            p2[i] = p_max
        print(p1)
        print(p2)
        pnl_max = 0
        for i in range(len_px):
            if p1[i]+p2[i] > pnl_max:
                pnl_max = p1[i]+p2[i]
        return pnl_max


a = [7,6,4,3,1]   
msol = Solution()
print(msol.maxProfit(a)) 
        
        