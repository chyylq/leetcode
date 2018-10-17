'''
Created on Oct 5, 2018

@author: Q
sparse matrix
so if a[i][j]!=0, we should do all the calc for a[i][j] with b[j][k] (k=0...)
and add the result in c[i][k] (k=0....) 
'''
class Solution:
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        nrow = len(A)
        ncol = len(B[0])        
        ret = [[0]*ncol for i in range(nrow)]
        tcol = len(A[0])
        
        for i in range(nrow):
            for j in range(tcol):
                if A[i][j]!=0:
                    for k in range(ncol):
                        if B[j][k] != 0:
                            ret[i][k] += A[i][j] * B[j][k]
        
        return ret