'''
Created on Aug 16, 2020

@author: Q

1. sort
2. triple loop, 4 pointers
   1st pointer from start, 2nd pointer from 2nd place, 3rd pointer from 3rd, 4th pointer from end
   loop by move 1st forward, 
   loop by keep 1st unchange, 2nd forward, loop by moving 3rd forward or 4th backward
   loop by keep 1st and 2nd unchange, moving 3rd forward or 4th backward

'''
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ret = set()
        nums = sorted(nums)
        cnt = len(nums)
        if cnt<4: return ret                
        for pt1 in range(0, cnt-3):
            for pt2 in range(pt1+1, cnt-2):
                pt3 = pt2+1
                pt4 = cnt-1
                while (pt3<pt4):
                    sums = nums[pt1]+nums[pt2]+nums[pt3]+nums[pt4] 
                    if sums == target:
                        ret.add((nums[pt1],nums[pt2],nums[pt3],nums[pt4]))
                        #print(pt1, pt2, pt3, pt4)
                        if nums[pt3+1] == nums[pt3]:
                            pt3 += 1
                        elif nums[pt4-1] == nums[pt4]:
                            pt4 -= 1
                        else:
                            pt3 += 1
                            pt4 -= 1
                    elif sums > target:
                        pt4 -= 1
                    elif sums < target:
                        pt3 += 1 
        return list(ret)
    
                
nums = [1, 0, -1, 0, -2, 2]
target = 0
msol = Solution()
print(msol.fourSum(nums, target))                    
                    