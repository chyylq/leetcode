from collections import defaultdict 

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        d = defaultdict(int) # use as a counter no 0 numbers
        d0 = 0  # counter for 0
        nums_one0 = []
        
        for k in nums:
            if k==0:
                d0 += 1      
                if (d0==1):
                    nums_one0.append(k)
            elif (k!=0) and d[k]<3:
                nums_one0.append(k)
                d[k] += 1
                
                
        sol = set()
        
        # 0's
        # 3 0's
        if d0 >= 3:             
            sol.add(tuple([0,0,0])) 
        
        # then only 1 0 is needed for a valid sol
        if d[0]>=1:
            d[0] = 1
        
        for i in range(len(nums_one0)):
            d[nums_one0[i]] = d[nums_one0[i]] - 1
            for j in range(i+1,len(nums_one0)):                
                d[nums_one0[j]] = d[nums_one0[j]] - 1
                if (-(nums_one0[i]+nums_one0[j]) in d) and (d[-(nums_one0[i]+nums_one0[j])]>0):
                    sol.add(tuple(sorted([nums_one0[i], nums_one0[j], -(nums_one0[i]+nums_one0[j])])))                    
                d[nums_one0[j]] = d[nums_one0[j]] + 1
            d[nums_one0[i]] = d[nums_one0[i]] + 1
        return list(sol)    