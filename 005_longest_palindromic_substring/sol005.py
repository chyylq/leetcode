'''
Created on Jul 26, 2020

@author: Q

DP, not the usually DP that moves 1 step forward along the string.
add # to deal with both odd and even mirror case

LP[i, j]
=  LP[i+1,j-1]+2                if s[i] == s[j] and LP[i+1,j-1]>0
   0                            else


'''
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """                
        if len(s) == 0: return ""
        
        s = "#".join(s[i:i+1] for i in range(len(s)))
        dim = len(s)
        a = [[0]*dim for i in range(dim)]
                                
        # initial from single char
        for i in range(dim):
            a[i][i] = 1
        ret = s[0]
        
        #print(s)
        # only fill half matrix
        # fill diagonally starting from next to the longest diagonal
        for k in range(1,dim): 
            for i in range(0, dim-k):                           
                j = i+k        
                if s[i] == s[j] and a[i+1][j-1]>0:
                    a[i][j] = a[i+1][j-1] + 2
                    if len(s[i:j+1].replace('#','')) > len(ret): 
                        ret = s[i:j+1].replace('#','')
                else:
                    a[i][j] = 0                    
        
        #print(a)
        return ret

         
m = Solution()
inp = "aaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxyyyyyyyyyyzzzzzzzzzzyyyyyyyyyyxxxxxxxxxxwwwwwwwwwwvvvvvvvvvvuuuuuuuuuuttttttttttssssssssssrrrrrrrrrrqqqqqqqqqqppppppppppoooooooooonnnnnnnnnnmmmmmmmmmmllllllllllkkkkkkkkkkjjjjjjjjjjiiiiiiiiiihhhhhhhhhhggggggggggffffffffffeeeeeeeeeeddddddddddccccccccccbbbbbbbbbbaaaaaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxyyyyyyyyyyzzzzzzzzzzyyyyyyyyyyxxxxxxxxxxwwwwwwwwwwvvvvvvvvvvuuuuuuuuuuttttttttttssssssssssrrrrrrrrrrqqqqqqqqqqppppppppppoooooooooonnnnnnnnnnmmmmmmmmmmllllllllllkkkkkkkkkkjjjjjjjjjjiiiiiiiiiihhhhhhhhhhggggggggggffffffffffeeeeeeeeeeddddddddddccccccccccbbbbbbbbbbaaaa" #"babad" "cbbd"
print(m.longestPalindrome(inp))
        