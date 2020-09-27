'''
Created on Sep 26, 2020

@author: Q

construct the sequence directly

'''

class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """        
        len_str = len(str(n))
        num_str = ' '*len_str         
        l = []
        cur_digit_pos = -1
        for _ in range(n):              
            # initial 1
            if cur_digit_pos==-1:
                cur_digit_pos = cur_digit_pos+1
                num_str = num_str.replace(' ', '1', 1)
                l.append(int(num_str))            
            # after it just moves tenth, there are 0's to the left, pad 0's
            elif (cur_digit_pos+1<=len_str-1) and num_str[cur_digit_pos+1]==' ' and int(num_str.replace(' ', '0', 1))<=n:
                cur_digit_pos = cur_digit_pos+1   
                num_str = num_str.replace(' ', '0', 1)             
                l.append(int(num_str))
            # if add 1, remove any trailing 0's
            elif int(str(int(num_str.replace(' ', '')) + 1).rstrip('0')) <= n:
                str_cur_num = str(int(num_str.replace(' ', '')) + 1).rstrip('0')
                cur_digit_pos = len(str_cur_num)-1
                num_str = str_cur_num.ljust(len_str, ' ')                     
                l.append(int(num_str))
            # a new digit to the left, need to set the reset all the right digits
            elif int(str((int(num_str[0:-1])+1)).rstrip('0')) <= n:                
                num_str = str(int(num_str[0:-1])+1).rstrip('0').ljust(len_str, ' ')
                cur_digit_pos = len(str(int(num_str[0:-1])+1).rstrip('0'))-1 
                l.append(int(num_str))
        return l

n = 193
msol = Solution()
print(msol.lexicalOrder(n))

            
                    
                    
            
            