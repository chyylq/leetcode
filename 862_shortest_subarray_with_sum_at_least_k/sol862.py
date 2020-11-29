'''
Created on Nov 29, 2020

@author: Q
'''
from collections import deque

class Solution(object):
    def shortestSubarray(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        if len(A)<1: 
            return -1
        dq = deque()        
        B = [0] * (len(A)+1)        
        for i in range(1,len(B)):            
            B[i] = B[i-1]+A[i-1]
        short_len = len(A)+1        
        for i in range(0,len(B)):
            # subtrahend: removing the element if it meets the condition
            # all smaller ones are removed b/c any future added number's location will be larger than the current and not suffice
            # equivalent to finding the nearest previous element that meets B[i]-B[j]>=K                        
            while len(dq)>0 and B[i]-B[dq[-1]]>=K:
                short_len = min(short_len, i-dq.pop())
            # minuend: removing the element if it is bigger
            # the current one should be at the top b/c we start treating as subtrahend, 
            # any number in the queue that is larger than the current will cause the distance to be larger with a newly added minuend in the future
            while len(dq)>0 and B[dq[0]]>=B[i]:
                dq.popleft()
            dq.appendleft(i)            
        return short_len if short_len<len(A)+1 else -1


m = Solution()            
A = [1]
K = 1 #4
print(m.shortestSubarray(A,K))  
                
            
                    
            
