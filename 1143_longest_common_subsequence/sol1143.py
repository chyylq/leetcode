'''
Created on Sep 20, 2020

@author: Q
'''
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        n1 = len(text1)
        n2 = len(text2)
        lcs = [[0 for _ in range(n2)] for _ in range(n1)]
        if text1[0]==text2[0]: lcs[0][0] = 1
        for i in range(1, n1):            
            lcs[i][0] = max(lcs[i-1][0], 1 if text1[i]==text2[0] else 0)
        for j in range(1, n2):
            lcs[0][j] = max(lcs[0][j-1], 1 if text1[0]==text2[j] else 0)
        for i in range(1,n1):
            for j in range(1,n2):                
                lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1], lcs[i-1][j-1]+1 if text1[i]==text2[j] else lcs[i-1][j-1])
        #print (lcs)
        return lcs[n1-1][n2-1]

text1 = "abc"
text2 = "efg" 
msol = Solution()
print(msol.longestCommonSubsequence(text1, text2))

        