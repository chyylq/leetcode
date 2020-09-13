'''
Created on Sep 13, 2020

@author: Q

similar to 005
and mask the cell a[i,j] to 1 if [i,j] forms a palindromic string
'''
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # add # 
        if len(s)==0: return 0
        
        s = "#".join(s[i:i+1] for i in range(len(s)))
        dim = len(s)
        a = [[0]*dim for i in range(dim)]
        
        total = 0
        # initialization and count
        for i in range(dim):        
            a[i][i] = 1
            if s[i] != '#':
                total += 1
        
        # DP and count
        for i in range(dim-1,0,-1):
            for j in range(i,dim,1):
                #print (i,j, s[i-1], s[j+1])                
                if (i-1)>=0 and (j+1)<dim and s[i-1]==s[j+1] and a[i][j]==1:                    
                    a[i-1][j+1]=1
                    if s[i-1]!='#':
                        total += 1
        
        #print(a)
        return total
        
a = "a"
msol = Solution()
print(msol.countSubstrings(a))  
        
                     
        