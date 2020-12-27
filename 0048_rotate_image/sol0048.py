'''
Created on Dec 27, 2020

@author: Q

rotate the four elements in (left,up),(up,right),(right,bottom),(bottom,left) parts each time
the indices relationship:  m[i][j] -> m[j][N-1-i]
'''
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        for i in range(0, N//2 + N%2):
            for j in range(0, N//2):                
                r, c = i, j
                tmp = matrix[r][c]
                for _ in range(4):                    
                    tmp, matrix[c][N-1-r] = matrix[c][N-1-r], tmp                                        
                    r, c = c, N-1-r
                
msol = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
ares = msol.rotate(matrix)
print(matrix)              