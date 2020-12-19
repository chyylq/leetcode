'''
Created on Dec 19, 2020

@author: Q
'''
class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """               
        def compute(input):
            """
            divide and conquer
            """
            l = []
            if ('+' not in input) and ('-' not in input) and ('*' not in input):
                l.append(int(input))                
            else:                
                i = 0
                while (i < len(input)):
                    operator = input[i]
                    x = input[0:i]
                    y = input[i+1:]
                    if operator == '+':
                        for s1 in compute(x):
                            for s2 in compute(y):
                                l.append(s1+s2)
                    elif operator == '-':
                        for s1 in compute(x):
                            for s2 in compute(y):
                                l.append(s1-s2)
                    elif operator == '*':
                        for s1 in compute(x):
                            for s2 in compute(y):
                                l.append(s1*s2)
                    else:
                        pass
                    i = i+1
            return l        
        
        def compute2(input):
            """
            dp[m,n] 
            results that start from mth number and ends nth number
            fill the table diagonal in each run
            for each element loop operator within positions i, j
            """
            s = [int(x) for x in input.replace('+',' ').replace('*',' ').replace('-', ' ').split(' ')]
            n = len(s)
            operators = []
            for x in input:
                if x in ('+-*'):
                    operators.append(x)
            dp = [[[] for _ in range(n)] for _ in range(n)]
            for i in range(n):
                j, k = 0, i
                while (k<n):
                    if (j==k):
                        dp[j][k].append(s[j])
                    else:
                        for l in range(j,k):
                            for x in dp[j][l]:
                                for y in dp[l+1][k]:
                                    if operators[l]=='+':
                                        dp[j][k].append(x+y)
                                    elif operators[l]=='-':
                                        dp[j][k].append(x-y)
                                    elif operators[l]=='*':
                                        dp[j][k].append(x*y)
                    j = j+1
                    k = k+1
            
            #print(dp)
            return dp[0][n-1]
        
        return compute2(input)    

msol = Solution()
s = '2*3-4*5'
ares = msol.diffWaysToCompute(s)
print(ares)        