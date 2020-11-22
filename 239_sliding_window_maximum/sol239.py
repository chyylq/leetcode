'''
Created on Nov 22, 2020

@author: Q

monotonic queue len is k
a queue which has the elements as first value in order with second value indicating the array range between the current element's position and the one before it in the queue
the positions of the element in the original array are all behind the positions of the element before it in the queue  
O(1) to get max
O(k) to push at the end of queue - the element before is larger than the current val 
and truncate smaller elements in the queue b/c in the current window the smaller elements are all before the current position and have no chance to be selected  
the count is increased by the number elements that are truncated
O(1) to pop - decrease the top count till is 0 then remove
'''
from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dq = deque()        
        res = []        
        # initial
        for i in range(len(nums)):
            cnt = 0
            # remove element from the left
            if i>k-1 and len(dq)>0:
                if dq[0][1]>0:
                    dq[0][1] = dq[0][1]-1
                else:
                    dq.popleft()
            # append element from the right
            while len(dq)>0:
                if dq[-1][0] < nums[i]:
                    cnt = cnt+dq[-1][1]+1
                    dq.pop()
                else:
                    break
            dq.append([nums[i], cnt])
            # get the max
            if i>=k-1:
                res.append(dq[0][0])
            print(dq)    
        return res

m = Solution()            
nums = [-7,-8,7,5,7,1,6,0]#[9,11]#[1,3,-1,-3,5,3,6,7]
k = 4
print(m.maxSlidingWindow(nums, k))   
            
        
                    
                
                
        
        