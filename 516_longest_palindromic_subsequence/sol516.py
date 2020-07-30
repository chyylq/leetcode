'''
Created on Jul 26, 2020

@author: Q

DP, not the usually DP that moves 1 step forward along the string.

LP[i, j]
=  LP[i+1, j-1] + 2                if s[i] == s[j]
   MAX( LP[i+1, j], LP[i, j-1] )   else


'''
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        dim = len(s)
        a = [[0]*dim for i in range(dim)]
        if dim == 0: return 0
        
        # initial from single char
        for i in range(dim):
            a[i][i] = 1
        ret = 1
        # only fill half matrix
        # fill diagonally starting from next to the longest diagonal
        for k in range(1,dim): 
            for i in range(0, dim-k):                           
                j = i+k        
                if s[i] == s[j]:
                    a[i][j] = a[i+1][j-1] + 2
                    ret = a[i][j]
                else:
                    if a[i+1][j] > a[i][j-1]:
                        a[i][j] = a[i+1][j]
                    else:
                        a[i][j] = a[i][j-1]
        
        return ret

         
m = Solution()
inp = "bbbab" #"babad" "cbbd"
print(m.longestPalindrome(inp))
        