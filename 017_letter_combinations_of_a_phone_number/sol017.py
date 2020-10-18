'''
Created on Oct 17, 2020

@author: Q
'''
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """        
        if len(digits)==0: return []
        
        letter_map = {'2':['a','b','c'],
         '3':['d','e','f'],
         '4':['g','h','i'],
         '5':['j','k','l'],
         '6':['m','n','o'],
         '7':['p','q','r','s'],
         '8':['t','u','v'],
         '9':['w','x','y','z'],}
                
        def func(digits):
            if len(digits)==0:
                return ['']
            return [x + y for x in letter_map[digits[0]] for y in func(digits[1:])]
            '''
            l = []
            for x in range(3):
                yfunc = func(digits[1:])
                for y in yfunc:
                    l.append(chr(x+ 3*letter_offset + letter_base + d) + y)
            return l
            '''
        return func(digits)



msol = Solution()
digits = "23"
print(msol.letterCombinations(digits))       