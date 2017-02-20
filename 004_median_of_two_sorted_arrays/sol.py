# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 16:41:52 2017

logic:
each time throw front or back # records in each array based on 2 medians
# records is ~ half of the smaller array
still keeps median or median decision elements -- central neighbors of an even array
discuss when the smaller array has 0,1,2 elements

other sols:
same: 
http://www.geeksforgeeks.org/median-of-two-sorted-arrays-of-different-sizes/

different (better): 
https://discuss.leetcode.com/topic/16797/very-concise-o-log-min-m-n-iterative-solution-with-detailed-explanation/2

@author: Q
"""
import sys

def findMedianSortedArrays2(nums1, nums2):
    N1, N2 = len(nums1), len(nums2)
    if N1 < N2: 
        nums1, N1, nums2, N2 = nums2, N2, nums1, N1
    l, r = 0, N2*2
    while l <= r:
        j = (l + r) >> 1
        i = N1 + N2 - j
        L1 = -sys.maxint-1 if i == 0 else nums1[(i-1)>>1]
        L2 = -sys.maxint-1 if j == 0 else nums2[(j-1)>>1]
        R1 = sys.maxint if i == 2*N1 else nums1[i>>1]
        R2 = sys.maxint if j == 2*N2 else nums2[j>>1]
        if L1 > R2: l = j + 1
        elif L2 > R1: r = j - 1
        else:
            return (max(L1, L2) + min(R1, R2))/2.0


class Solution(object):
    
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
            
        def getMedian(p):
            l = (len(p)-1)/2
            r = len(p) / 2
            return 0.5*(p[l]+p[r])
       
       # median index  = (L + R)/2
        len1 = len(nums1)
        len2 = len(nums2)
        if (len2 < len1):
            return self.findMedianSortedArrays(nums2, nums1)
        
        # use l(eft), r(ight)
        # if array is odd, l, r is same as median
        # if array is even, l, r is center neighbors
        l1 = (len(nums1)-1)/2
        r1 = len(nums1) / 2
        l2 = (len(nums2)-1)/2
        r2 = len(nums2) / 2
        
        if (len1 == 0) and (len2 > 0):
            # nums1 empty
            return getMedian(nums2)
        elif len1 == 1:
            # nums1 has 1 element
            if (len2 % 2 ==0):
                # nums2 is even, return the median of 3
                if nums1[0] <= nums2[l2]: 
                    return 1.0*nums2[l2]
                elif nums2[r2] <= nums1[0]:
                    return 1.0*nums2[r2]
                else:
                    return 1.0*nums1[0]
            else:
                # nums2 is odd, return median of the 2
                if len2 == 1:
                    return 0.5*(nums1[0]+nums2[0])
                elif nums1[0] <= nums2[l2-1]:
                    return 0.5*(nums2[l2-1]+nums2[l2])
                elif nums2[l2+1] <= nums1[0]:
                    return 0.5*(nums2[l2]+nums2[l2+1])
                else:
                    return 0.5*(nums1[0]+nums2[l2])
        elif len1 == 2:
            # nums1 has 2 elements, discuss
            if (len2 % 2 ==0):
                if len2 == 2:
                    nums2.insert(0,-sys.maxint-1)
                    nums2.append(sys.maxint)
                    l2 = (len(nums2)-1)/2
                    r2 = len(nums2) / 2
                    
                if nums1[1] <= nums2[l2-1]:
                    return 0.5*(nums2[l2-1]+nums2[l2])
                elif nums2[l2-1] < nums1[1] and nums1[1] <= nums2[r2]:
                    if nums1[0] <= nums2[l2]:
                        return 0.5*(nums2[l2]+nums1[1])
                    else:
                        return 0.5*(nums1[0]+nums1[1])
                elif nums2[r2] < nums1[1]:
                    if nums1[0] <= nums2[l2]:
                        return 0.5*(nums2[l2]+nums2[r2])
                    elif nums2[l2] < nums1[0] and nums1[0] <= nums2[r2+1]:
                        return 0.5*(nums1[0]+nums2[r2])
                    else:
                        return 0.5*(nums2[r2]+nums2[r2+1])
            else:
                if nums1[1] <= nums2[l2-1]:
                    return 1.0*nums2[l2-1]
                elif nums1[1] <= nums2[l2]:
                    return 1.0*nums1[1]
                else:
                    if nums1[0] <= nums2[l2]:
                        return 1.0*nums2[l2]
                    elif nums1[0] <= nums2[l2+1]:
                        return 1.0*nums1[0]
                    else:
                        return nums2[l2+1]
                
        elif getMedian(nums1) == getMedian(nums2):
            # if median of nums1 = median of nums2, solution is found
            return getMedian(nums1)    
        elif getMedian(nums1) < getMedian(nums2):
            # median nums1 < median nums2
            # remove 1st half in nums1 and same # elements in nums2 backwards
            # if nums1 is odd, remove till the one before median, keep median
            # if nums1 is even, remove till the left central-1, keep left central
            # to keep median or left central is to not throw away median decision elements
            return self.findMedianSortedArrays(nums1[l1:], nums2[:len2-l1])            
        elif getMedian(nums1) > getMedian(nums2):
            # median nums1 > median nums2
            # remove 2nd half in nums1 and same # elements in nums2 at the front
            # if nums1 is odd, remove from the one after median, keep till median
            # if nums1 is even, remove from the right central+1, keep till right central
            return self.findMedianSortedArrays(nums1[:r1+1], nums2[len1-r1-1:])
    
        
        
        
nums1 = [1, 3, 7 ,9, 10, 11]
nums2 = [2,2]   


sol = Solution()
b = sol.findMedianSortedArrays(nums1, nums2)
c = findMedianSortedArrays2(nums1, nums2)
