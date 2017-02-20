# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 16:41:52 2017

@author: Q
"""
import sys

 def findMedianSortedArrays(nums1, nums2):
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
   
# median index  = (L + R)/2
# use L, R to repsent median to deal with both odd and even length
def findMedianSortedArrays_Sol(M, N):
    print M, N
    len1 = len(M)
    len2 = len(N)
    
    l1 = (len1-1) / 2
    r1 = (len1) / 2
    l2 = (len2-1) / 2
    r2 = (len2) / 2
    
    if (len1 == 0) and (len2 > 0):
        # M empty 
        return 1.0*(N[l2]+N[r2])/2
    elif (len1 > 0) and (len2 == 0):
        # N empty 
        return 1.0*(M[l1]+M[r1])/2
    elif (len1 == 0) and (len2 == 0):
        # both empty
        return None
    elif (len1 == 1) and (len2 == 1):
        return 1.0*(M[l1]+N[l2])/2
    elif ((M[l1]+M[r1]) == (N[l2]+N[r2])):
        # if median of M = median of N, solution is found
        return 1.0*(M[l1]+M[r1])/2    
    elif ((M[l1]+M[r1]) < (N[l2]+N[r2])):
        # median M < median N
        # remove 1st half in M and 2nd half in N
        return findMedianSortedArrays_Sol(M[r1:], N[:l2+1])
    elif ((M[l1]+M[r1]) > (N[l2]+N[r2])):
        # median M > median N
        # remove 2nd half in M and 1st half in N
        return findMedianSortedArrays_Sol(M[:l1+1], N[r2:])
    else:
        print 'error'


nums1 = [1, 3, 7 ,9, 10, 11]
nums2 = [2,2]   

nums1 = range(3,12)
nums2 = range(1,3)

a = findMedianSortedArrays_Sol(nums1, nums2)
b = findMedianSortedArrays(nums1, nums2)
