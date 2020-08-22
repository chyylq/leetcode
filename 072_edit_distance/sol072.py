'''
Created on Aug 22, 2020

@author: Q

dp
edit[s,t] represent the #edits for w1[0:t] and w2[0:s]
w1_used[i] represent w1's ith char has a match already or not
w2_used[s] represent w2's jth char has a match already or not
edit[s,t] = min (edit[s-1,t]     if w1[t]==w2[s] and w1_used[t]==0,  else edit[s-1,t]+1 for replace 
                 edit[s-1,t-1]   if w1[t]==w2[s]                     else edit[s-1,t-1]+1 for replace
                 edit[s,t-1])    if w1[t]==w2[s] and w2_used[s]==0,  else edit[s,t-1]+1 for replace
'''

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """        
        row_cnt = len(word2)
        col_cnt = len(word1)
        if row_cnt==0: return col_cnt
        if col_cnt==0: return row_cnt
        edit = [[0 for i in range(col_cnt)] for j in range(row_cnt)]
        w2_used = [0 for i in range(row_cnt)]
        w1_used = [0 for i in range(col_cnt)]
        
        if word1[0]==word2[0]:            
            w1_used[0]=1
            w2_used[0]=1
        else:
            edit[0][0]=1
        
        for i in range(1,row_cnt):
            if word1[0]==word2[i] and w1_used[0]==0:
                edit[i][0]=edit[i-1][0]
                w1_used[0]=1
            else:
                edit[i][0]=edit[i-1][0]+1
        for j in range(1,col_cnt):
            if word2[0]==word1[j] and w2_used[0]==0:
                edit[0][j]=edit[0][j-1]
                w2_used[0]=1
            else:
                edit[0][j]=edit[0][j-1]+1
        for i in range(1,row_cnt):
            for j in range(1,col_cnt):
                #print(i,j)
                if word1[j]==word2[i] and w1_used[j]==0:
                    v1 = edit[i-1][j]
                    w1_used[j]=1
                else:
                    v1 = edit[i-1][j] + 1
                if word1[j]==word2[i] and w2_used[i]==0:
                    v3 = edit[i][j-1]
                    w2_used[i]=1
                else:
                    v3 = edit[i][j-1] + 1
                if word1[j]==word2[i]:
                    v2 = edit[i-1][j-1]
                    w1_used[j]=1
                    w2_used[i]=1
                else:
                    v2 = edit[i-1][j-1] + 1
                #print(v1,v2,v3)
                edit[i][j] = min(v1,v2,v3)
        
        #print (edit)
        return edit[row_cnt-1][col_cnt-1]
    

word1 = "intention" #"horse"
word2 = "execution" #"ros"
msol = Solution()
print(msol.minDistance(word1, word2))        
                
         