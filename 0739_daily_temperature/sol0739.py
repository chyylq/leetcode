'''
Created on Dec 27, 2020

@author: Q

monotonic queue
'''

class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        q = list()
        res = [0] * len(T)
        for i in range(len(T)):
            if len(q)==0:
                q.append(i)
            elif T[i]<=T[q[-1]]:
                q.append(i)
            else:
                while (len(q)>0) and (T[i]>T[q[-1]]):
                    cur_idx = q.pop()
                    dist = i-cur_idx
                    res[cur_idx] = dist
                q.append(i)
        return res

msol = Solution()
nums = [73, 74, 75, 71, 69, 72, 76, 73]
ares = msol.dailyTemperatures(nums)
print(ares)      
                    
                