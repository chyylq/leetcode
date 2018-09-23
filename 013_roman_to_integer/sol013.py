'''
Created on Sep 22, 2018

@author: Q
'''
class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d_roman_to_int = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        l_pos = ['I','V','X','L','C','D','M']
        val = 0
        for i, ch in enumerate(s):            
            sig = 1
            if i<len(s)-1:                
                if ch in ('I','X','C') and (l_pos.index(s[i+1])>l_pos.index(s[i])) and (l_pos.index(s[i+1])<=(2+l_pos.index(s[i]))):
                    sig = -1                                
            val = val + sig * d_roman_to_int[ch]            
            print(val)
        return val
    
    
    
    
a = "MCMXCIV"    
msol = Solution()
print(msol.romanToInt(a))