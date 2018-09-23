'''
Created on Sep 22, 2018

@author: Q
'''
class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        l = path.split('/')
        sp = []
        for p in l:
            if p in ('', '.'):
                continue
            elif p == '..':
                if len(sp)>=1:
                    sp = sp[0:-1]
                else:          
                    sp.append('#')
            else:
                sp.append(p)
            print(sp)    
        sp = '/'+'/'.join(sp)
        idx = sp.rfind('#')
        if idx<(len(sp)-1):
            return sp[(idx+1):]
        else:
            return '/'


a = "/a/./b///../c/../././../d/..//../e/./f/./g/././//.//h///././/..///" 
msol = Solution()
print(msol.simplifyPath(a)) 