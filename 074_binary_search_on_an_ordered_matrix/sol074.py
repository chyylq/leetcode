'''
Created on Aug 9, 2020

@author: Q
'''
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        r = len(matrix)
        if r>0:
            c = len(matrix[0])
        else:
            return False
        s_i, s_j = 0, 0
        e_i, e_j = r-1, c-1
        head = s_i*c + s_j
        tail = e_i*c + e_j
        if (target==matrix[s_i][s_j]) or (target==matrix[e_i][e_j]):
            return True        
        while (head<=tail):            
            npt = (head + tail ) // 2
            m_i = npt // c
            m_j = npt%c       
            print(m_i, m_j)
            if (target==matrix[m_i][m_j]):
                return True
            elif (target>matrix[m_i][m_j]):
                s_i, s_j = m_i, m_j
                head = s_i*c + s_j + 1              
            elif (target<matrix[m_i][m_j]):
                e_i, e_j = m_i, m_j
                tail = e_i*c + e_j - 1
            
        return False

a = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
msol = Solution()
print(msol.searchMatrix(a, 3))
    