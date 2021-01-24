'''
Created on Jan 24, 2021

@author: Q
backtrack + memoization
'''
class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        self.memo = {}
                
        def checkParenthesis(s, i, stack):
            if (i,stack) in self.memo:
                return self.memo[(i,stack)]
            if i==len(s) and len(stack)==0:
                self.memo[(i,stack)]=True
                return True
            elif i==len(s) and len(stack)>0:
                self.memo[(i,stack)]=False
                return False
            elif i<len(s):                
                if s[i]==')':
                    if len(stack)>0 and stack[-1]=='(':
                        res = checkParenthesis(s, i+1, stack[0:-1])
                        self.memo[(i+1,stack[0:-1])]=res
                        return res
                    else:
                        self.memo[(i,stack)]=False
                        return False
                elif s[i]=='(':
                    res = checkParenthesis(s, i+1, stack+s[i])
                    self.memo[(i+1,stack+s[i])]=res             
                    return res
                else:
                    res = any([checkParenthesis(s, i+1, stack), # treat * as empty
                               checkParenthesis(s[0:i]+'('+s[i+1:], i, stack), # treat * as (
                               checkParenthesis(s[0:i]+')'+s[i+1:], i, stack)  # treat * as )
                               ])                                 
                    return res
                 
        return checkParenthesis(s, 0, '')

msol = Solution()
s = "(*))"
ares = msol.checkValidString(s)
print(ares)                     