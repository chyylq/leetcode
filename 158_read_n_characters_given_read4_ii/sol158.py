'''
Created on Oct 6, 2018

@author: Q
'''
# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):
str0 = 'ab'
cur_idx = 0

def read4(buf4):
    global cur_idx   
    idx = cur_idx
    for i in range(idx, min(idx+4, len(str0))):
        buf4[i] = str0[cur_idx]
        cur_idx += 1            
    return cur_idx-idx

class Solution(object):    
    def __init__(self):
        self.buff = [] # the whole read-in buff from read4
        self.idx = 0 # the last read position, can be shorter than len of buff b/c read len is not 4's multiple
        
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        # use read4 to read all data into the buff up till n up
        idx0, idx1 = self.idx, self.idx        
        while (idx1<=idx0+n-1):    
            buf4 = ['']*4        
            cnt4 = read4(buf4)                        
            if cnt4==0: 
                break        
            buff4 = [x for x in buf4 if x!='']     
            self.buff.extend(buff4)
            idx1 += len(buff4)
        # return from the latest pointer to the min of length from current string or requested input                             
        for i in range(idx0, min(len(self.buff), idx0+n)):
            #print(i)
            buf[i-idx0] = self.buff[i]
            self.idx += 1                
        return self.idx-idx0  
        
m = Solution()
buf0 = ['','','','']
print(m.read(buf0, 2))
print(buf0) 
print('next..')
print(m.read(buf0, 1))
print(buf0)
print('next..')
print(m.read(buf0, 1))
print(buf0)
