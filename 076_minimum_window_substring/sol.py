# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 14:23:38 2018

if all T are in the current window, look at the length
Once all T are in current window,
if encounter character C the first time when moving the window end, calc window length.
if encouter character C the last time when moving the window start, calc window length.
the idea is that we can ignore multiple occurrence when all T is in the current window

to achieve O(n)
we need start pionter, end pointer 
a map showing the occurence of each char in the current window
and a counter only updates when item in the map is in or not in at the moment to show if all T are present
@author: yilin
"""
import collections
import sys

class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        map_char_target = collections.Counter(t)
        map_char = dict()
        for k in map_char_target.keys():
            map_char[k] = 0
        target = len(map_char)
        start, end, min_len, win_start, win_end, counter = 0, 0, sys.maxsize, 0, -1, 0
        while (end<len(s)):    
            if s[end] in map_char:
                map_char[s[end]] += 1
                if map_char[s[end]] == map_char_target[s[end]]:
                    counter += 1
                    #print (counter, start, end)
            while (counter==target):
                print (start, end, counter, map_char, map_char_target)
                if end-start<min_len:
                    win_start, win_end, min_len = start, end, end-start
                if s[start] in map_char:
                    map_char[s[start]] -= 1
                    #print (map_char)
                    if map_char[s[start]] == (map_char_target[s[start]]-1):
                        counter -= 1
                #print (counter)
                start += 1
            end += 1
        return s[win_start: win_end+1] 
    def minWindow2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """        
        l,r,winsz = 0,0,len(s)+1
        res = ''
        t_char = Counter(t)
        t_win_char = {}
        for x in t_char:
            t_win_char[x] = 0
        total_cnt = len(t_char)
        while r<len(s):
            cur_char = s[r]
            # update total count of candidate in current window
            if cur_char in t_win_char:
                t_win_char[cur_char] = t_win_char[cur_char]+1            
            if sum([t_win_char[k]>=t_char[k] for k in t_win_char])==total_cnt: 
                if r-l+1<winsz:
                    winsz = r-l+1
                    res = s[l:r+1]                
                while l<=r:
                    if sum([t_win_char[k]>=t_char[k] for k in t_win_char])==total_cnt and r-l+1<winsz:
                        winsz = r-l+1
                        res = s[l:r+1]
                    if s[l] in t_win_char:
                        t_win_char[s[l]] = t_win_char[s[l]]-1
                        if t_win_char[s[l]]<t_char[s[l]]:
                            l = l+1
                            break                    
                    l = l+1                        
            r = r+1
        return res   

m = Solution()
S = "cabwefgewcwaefgcf"##'ADOBECODEBANC'
T = "cae"#'ABC'
print(m.minWindow(S,T))

