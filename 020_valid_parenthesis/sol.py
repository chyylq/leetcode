# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 21:15:44 2018

@author: yilin
"""

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = list()
        for brac in s:
            if brac in ('{','[','('}):
                l.append(brac)
            elif len(l)==0:
                return False
            else:
                s_open = l.pop()
                if not ((brac=='}' and s_open=='{') or (brac==']' and s_open=='[') or (brac==')' and s_open=='(')):
                    return False
        if len(l)==0:
            return True
        else:
            return False