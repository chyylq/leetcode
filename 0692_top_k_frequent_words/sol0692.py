'''
Created on Apr 10, 2021

@author: Q
'''
from collections import defaultdict
from bisect import insort

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        hist, freq = defaultdict(int), defaultdict(list)
        for word in words:
            hist[word] += 1
        
        max_cnt = 0
        for word,cnt in hist.items():
            insort(freq[cnt],word)
            if cnt>max_cnt:
                max_cnt = cnt
        print(freq)
        
        res = []        
        for i in range(max_cnt,0,-1):
            res.extend(freq[i])
            if len(res)>=k:
                return res[0:k]
            
msol = Solution()
logs = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
k = 4
ares = msol.topKFrequent(logs, k)
print(ares)   
            
            