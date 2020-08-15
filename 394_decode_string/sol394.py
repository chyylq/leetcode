'''
Created on Aug 15, 2020

@author: Q
'''
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)==0: 
            return ''
        else:        
            return self.parse1set(s)
    
    def parse1set(self, s):
        print(s)
        s_new = ''
        s_inside_bracket = ''
        is_open = False
        is_out_close = 0
        multiplier = ''
        for i in range(len(s)):
            # handle the multiplier and brackets            
            if s[i].isdigit() and (not is_open):
                multiplier += s[i]
                continue
            elif s[i]=='[':
                is_out_close += 1
                if not is_open:
                    is_open = True
                    continue                
            elif s[i]==']':
                is_out_close -= 1
                if is_open and is_out_close==0:
                    break
            # handle chars
            if is_open:
                s_inside_bracket += s[i]
            else:
                s_new += s[i]
        
        if len(s_inside_bracket)>0:        
            return self.parse1set(s_new + int(multiplier)*s_inside_bracket + s[i+1:])
        else:
            return s
                    
                
s = "11[ab]e"
msol = Solution()
print(msol.decodeString(s))                    
                
        