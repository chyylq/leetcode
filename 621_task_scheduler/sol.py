# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 20:12:22 2018

@author: yilin
"""

class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        next_n_excl = [None for i in range(n)]
        #jobs = []
        n_jobs = 0
        d_count = dict()
        for i in tasks:
            if i not in d_count:
                d_count[i]=0
            d_count[i] += 1

        while sum(d_count.values())>0:
            is_add = False
            cur_elem = None
            #print(d_count)
            #print (next_n_excl)
            for kv in sorted(d_count.items(), key=lambda x:x[1], reverse=True):
                if len(next_n_excl)==0 or not kv[0] in next_n_excl:
                    #jobs.append(kv[0])
                    n_jobs += 1
                    d_count[kv[0]] -= 1
                    if d_count[kv[0]] == 0:
                        del d_count[kv[0]]
                    cur_elem = kv[0]
                    is_add = True
                    break
            if not is_add:
                #jobs.append('idle')
                n_jobs += 1
            
            if len(next_n_excl)>0:
                next_n_excl.pop(0)
                if is_add:
                    next_n_excl.append(cur_elem)
                else:
                    next_n_excl.append(None)
            #print(jobs)
        #print (jobs)
        return n_jobs
    
m = Solution()
tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
n = 2
print(m.leastInterval(tasks, n))