'''
Created on Oct 6, 2018

when read, need to make sure the cutoff is the min between the total length limit and read4 return length limit 

@author: Q
'''
# The read4 API is already defined for you.
# @param buf, a list of characters as what is the read output from the source
# @return an integer
# def read4(buf):

def read4(buf4):
    pass

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        idx = 0        
        while (idx<=n-1):
            buf4 = ['']*4
            cnt4 = read4(buf4)
            if cnt4==0: 
                break
            buf[idx:min(idx+cnt4,n)] = buf4[0:min(cnt4,n-idx)]
            idx = min(idx+cnt4, n)        
        return idx
            
        