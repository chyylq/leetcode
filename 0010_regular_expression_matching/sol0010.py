'''
Created on Jan 2, 2021

@author: Q

DP
'''

class Solution(object):
    def isMatch(self, s, p0):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        S, P0, P = len(s), len(p0), len(p0.replace('*','')) # adjust p by remove '*'
        if S==0 and P==0: return True        
        elif S>0 and P==0: return False
        # get '*' char
        is_star = set()
        p = ''
        for i in range(P0):
            if p0[i]!='*':
                p += p0[i]
            if i+1<P0 and p0[i+1]=='*':
                is_star.add(len(p)-1)            
        
        a = [[0 for _ in range(P+1)] for _ in range(S+1)]  # initial length+1 to deal with empty string cases        
        # initialize a[0,0]
        a[0][0] = 1
        for j in range(0, P):
            if j in is_star:
                a[0][j+1] = a[0][j]         
        #print(p)
        #print(is_star)
        for i in range(1, S+1):
            for j in range(1, P+1):
                #print(i,j)                
                if p[j-1] in (s[i-1],'.'):             # match char one by one for * char also match once
                    a[i][j] = a[i-1][j-1] | a[i][j]                
                if j-1 in is_star:
                    if p[j-1] in (s[i-1],'.'):         # if *, case for current p match one than once for same char in s - multiple matches
                        a[i][j] = a[i-1][j] | a[i][j]
                    a[i][j] = a[i][j-1] | a[i][j]      # if *, case for current p is omitted  - 0 match
                    
        print(a)
        if a[S][P]==1:
            return True
        else:
            return False
        
        
    def isMatch2(self, s, p):        
        # Initialize DP table
        # Row indices represent the lengths of subpatterns
        # Col indices represent the lengths of substrings
        T = [
            [False for _ in range(len(s)+1)]
            for _ in range(len(p)+1)
        ]

        # Mark the origin as True, since p[:0] == "" and s[:0] == ""
        T[0][0] = True

        # Consider all subpatterns p[:i], i > 0 against empty string s[:0]
        for i in range(1, len(p)+1):
            # Subpattern matches "" only if it consists of "{a-z}*" pairs
            T[i][0] = i > 1 and T[i-2][0] and p[i-1] == '*'

        # Consider the empty pattern p[:0] against all substrings s[:j], j > 0
        # Since an empty pattern cannot match non-empty strings, cells remain False

        # Match the remaining subpatterns (p[:i], i > 0) with the remaining
        # substrings (s[:j], j > 0)
        for i in range(1, len(p)+1):
            for j in range(1, len(s)+1):

                # Case 1: Last char of subpattern p[i-1] is an alphabet or '.'
                if p[i-1] == s[j-1] or p[i-1] == '.':
                    T[i][j] |= T[i-1][j-1]

                # Case 2: Last char of subpattern p[i-1] is '*'
                elif p[i-1] == '*':

                    # Case 2a: Subpattern doesn't need '*' to match the substring

                    # If the subpattern without '*' matches the substring,
                    # the subpattern with '*' must still match
                    T[i][j] |= T[i-1][j]

                    # If the subpattern without '*' and its preceding alphabet
                    # matches the substring, then the subpattern with them
                    # must still match
                    T[i][j] |= i > 1 and T[i-2][j]

                    # Case 2b: Subpattern needs '*' to match the substring

                    # If the alphabet preceding '*' matches the last char of
                    # the substring, then '*' is used to extend the match for
                    # the substring without its last char
                    if i > 1 and p[i-2] == s[j-1] or p[i-2] == '.':
                        T[i][j] |= T[i][j-1]

        return T[-1][-1]

msol = Solution()
s = "a"
p = ".*..a*"
ares = msol.isMatch(s,p)
print(ares)              
                                  
        