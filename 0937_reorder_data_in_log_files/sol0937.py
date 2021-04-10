'''
Created on Apr 10, 2021

@author: Q
'''
class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        def get_key(log):
            items = log.split(sep=' ', maxsplit=1)
            return (0, items[1], items[0]) if items[1][0].isalpha() else (1, None, None)
        
        return sorted(logs, key=get_key)
    
    
msol = Solution()
logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
ares = msol.reorderLogFiles(logs)
print(ares)     