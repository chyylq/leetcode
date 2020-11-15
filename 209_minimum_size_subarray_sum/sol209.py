'''
Created on Nov 15, 2020

@author: Q
start from 1, what's the first span for sum >= s
then any elements after only makes span bigger, no need to move beyond
then from 2, what's the first span for sum >= s
in this case, we can use the previous sum, sum-a[i] is up till pivot's sum, we just need to check this and beyond to find the first span for sum>=s
during the whole process, we keep the min span
'''
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n==0: return 0
        span = n+1        
        pivot = 0
        cumsum = nums[0]
        
        for i in range(n):                   
            if i>=1:
                cumsum = cumsum - nums[i-1]
            if cumsum>=s:
                for k in range(pivot, i-1, -1):
                    cumsum = cumsum - nums[k]
                    if cumsum<s:
                        pivot = k - 1
                        break                
            for k in range(pivot+1, n):
                cumsum += nums[k]
                if cumsum>=s:
                    cur_span = k - i + 1 
                    if span > cur_span:
                        span = cur_span
                    pivot = k
                    print (cumsum, i, k)
                    break
                if k==n-1:
                    return span if span<n+1 else 0
        return span if span<n+1 else 0 

s = 4
nums = [1,4,4]
m = Solution()
print(m.minSubArrayLen(s, nums))    
             
            