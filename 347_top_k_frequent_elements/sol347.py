'''
Created on Nov 8, 2020

@author: Q
first pass to construct {num: freq} 
second pass to construct {freq: [num1, num2]}
third pass to use the available max freq to go back 1 by 1 to construct the top K frequent numbers 
'''
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hist, freq = {}, {}
        # histogram of the numbers, value is number of appearance
        for n in nums:
            if n in hist:
                hist[n] += 1
            else:
                hist[n] = 1
        
        # histogram of frequency, value is list of the numbers that have the frequency
        max_freq = 0
        for m in hist:
            if hist[m] in freq:
                freq[hist[m]].append(m)
            else:
                freq[hist[m]] = [m]
            if hist[m] > max_freq:
                max_freq = hist[m]
        
        # start from the largest and go back to get the largest K using 1 <= K <= number of unique elements
        l = 0
        res = []
        print (freq)        
        for i in range(max_freq, 0, -1):
            if i in freq:
                for x in freq[i]:
                    res.append(x)
                    l += 1
                    if l==k:
                        return res
                
m = Solution()
l = [-1,-1]
k=1
print(m.topKFrequent(l, k))                
                