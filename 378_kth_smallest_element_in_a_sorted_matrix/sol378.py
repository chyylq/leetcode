'''
Created on Jul 26, 2020

@author: Q

a binary matrix showing what have been selected so far
an ascending list of current candidate
once the top candidate is selected
check its right and down element, for each of them if both the elemnt's up and left neighbors have been selected, it is inserted into the candidate list 
'''
import heapq

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        dim = len(matrix)
        sel_matrix = [[0] * dim for i in range(dim) ]
        cand_list = []
        
        if dim==0:
            return None
        
        
        for i in range(k):
            if i==0:
                heapq.heappush(cand_list, (matrix[0][0], 0, 0))
                
            val,r,c = heapq.heappop(cand_list)
            print((r,c,val))
            if i==k-1:
                return val
            
            sel_matrix[r][c] = 1
            if (c+1<dim):
                r_new = r
                c_new = c+1
                if ((r_new>0) and (sel_matrix[r_new-1][c_new]==1) and (sel_matrix[r_new][c_new-1]==1)) or ((r_new==0) and (sel_matrix[r_new][c_new-1]==1)):
                    heapq.heappush(cand_list, (matrix[r_new][c_new], r_new, c_new))
            if (r+1<dim):
                r_new = r+1
                c_new = c
                if ((c_new>0) and (sel_matrix[r_new][c_new-1]==1) and (sel_matrix[r_new-1][c_new]==1)) or ((c_new==0) and (sel_matrix[r_new-1][c_new]==1)):
                    heapq.heappush(cand_list, (matrix[r_new][c_new], r_new, c_new))
            
            #print(sel_matrix)
            #print(cand_list)    
            
            

m = Solution()
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
k = 8

print(m.kthSmallest(matrix, k))    