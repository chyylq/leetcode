'''
Created on Feb 13, 2021

@author: Q

backtracing
'''
class Solution(object):
    def do_search(self, m, n, board, mask, cur_pt, word):
        if len(word)==0: 
            return True
        for i,j in ((-1,0),(1,0),(0,-1),(0,1)):
            nxt_i, nxt_j = cur_pt[0]+i, cur_pt[1]+j
            if nxt_i>=0 and nxt_i<m and nxt_j>=0 and nxt_j<n and mask[nxt_i][nxt_j]==0 and board[nxt_i][nxt_j]==word[0]:
                mask[nxt_i][nxt_j] = 1
                if self.do_search(m, n, board, mask, (nxt_i,nxt_j), word[1:]):
                    return True
                mask[nxt_i][nxt_j] = 0
        return False  
            
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        n = len(board[0])
        mask = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0]:
                    mask[i][j] = 1
                    if self.do_search(m, n, board, mask, (i,j), word[1:]):
                        return True
                    mask[i][j] = 0
        return False
    
    
msol = Solution()
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word =  "SEE"
ares = msol.exist(board, word)
print(ares) 
        