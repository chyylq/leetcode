# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 14:35:01 2018

@author: yilin
"""
import math

class Solution:
    num_map = {0:'',1:'One ',2:'Two ',3:'Three ',4:'Four ',5:'Five ',6:'Six ',7:'Seven ',\
               8:'Eight ',9:'Nine ',10:'Ten ',11:'Eleven ',12:'Twelve ',13:'Thirteen ',\
               14:'Fourteen ',15:'Fifteen ',16:'Sixteen ',17:'Seventeen ',18:'Eighteen ',\
               19:'Nineteen ',20:'Twenty ',30:'Thirty ',40:'Forty ',50:'Fifty ',60:'Sixty ',\
               70:'Seventy ',80:'Eighty ',90:'Ninety '}
    unit_map = {0:'',1:'Thousand ',2:'Million ',3:'Billion '}
 
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        digits = len(str(int(num)))
        words = ''
        #print (num)
        if num == 0: return 'Zero'
        
        for i in range((digits-1)//3,-1,-1):
            curnum = num // math.pow(1000,i)
            num = num % math.pow(1000,i)
            #print(curnum)
            if curnum > 0:
                words = words + self.parse_num(curnum)
                words = words + self.unit_map[i]
        return words.strip()
        
    def parse_num(self, num):
        num = int(num)
        #print(num)
        if num==0:
            return ''
        elif num <= 20:
            return self.num_map[num]
        else:
            digits = len(str(num))
            cur_num = num // math.pow(10, digits-1)
            num = num % math.pow(10, digits-1)
            #print (cur_num, num, digits)
            if digits==3:
                return self.num_map[cur_num] + 'Hundred ' + self.parse_num(num)
            elif digits==2:
                return self.num_map[cur_num*10] + self.parse_num(num)

m = Solution()
print (m.numberToWords(30))
print (m.numberToWords(123450))