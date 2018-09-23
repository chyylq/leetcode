'''
Created on Sep 17, 2018

@author: Q
'''
from functools import reduce

class Solution:
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        # ipv4
        isIPV4 = False
        parts = str(IP).split('.')        
        if len(parts)==4:
            isIPV4 = True            
            for part in parts:
                #print(reduce(lambda x,y:x and y, [x>='0' and x<='9' for x in part]))
                if len(part)>1 and part[0]!='0' and reduce(lambda x,y:x and y, [x>='0' and x<='9' for x in part]) and int(part)>=0 and int(part)<=255:
                        continue
                elif len(part)==1 and part[0]>='0' and part[0]<='9':
                        continue    
                else:
                    isIPV4 = False
                    break
        
        # ipv6
        isIPV6 = False
        parts = str(IP).split(':')
        if len(parts)==8:
            isIPV6 = True
            for part in parts:
                if len(part)>0 and len(part)<=4 and \
                    reduce(lambda x,y: x and y, [(x>='0' and x<='9') or (x>='A' and x<='F') or (x>='a' and x<='f') for x in part]):
                    continue
                else:
                    isIPV6 = False
                    break
                
        if isIPV4: 
            return 'IPv4'
        elif isIPV6: 
            return 'IPv6'
        else:
            return 'Neither'
        
        

msol = Solution()
print (msol.validIPAddress("1.0.1."))
#print (msol.validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334"))
#print (msol.validIPAddress("256.256.256.256"))
        
                    