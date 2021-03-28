'''
Created on Mar 28, 2021

@author: Q

[ for start; ] for end
2 cases in the stack for jobs are running:

[ tm1(id1) [tm2](id2)   need add tm1 to id1 and add tm2 to id2
2 steps
when encountering [, add tm1 to id1
when encountering ], add tm2 to id2 
   
[ [tm1](id1)]    need add tm1 to id1

so need a stack to store func that has started
a prv_time indicates last time of the top of the stack
if it is a start and push to the stack, prv_time = start time pushed in
if it is a end and pop out of the stack, prv_time = end time +1
'''


class Solution(object):
    def exclusiveTime0(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        # slot time saves the cpu time for func starts at i
        slot_time = [0] * 100
        # output
        out = [0] * n
        q = list()
        for entry in logs:
            id, state, tm = entry.split(':')
            id = int(id)
            tm = int(tm)          
            if state=='start':
                q.append((id, tm))
            else:
                cur_id, cur_start = q.pop()
                if id==cur_id:
                    cur_tm = tm - cur_start+1
                    slot_time[cur_start] = cur_tm
                    out[id] += slot_time[cur_start] - sum(slot_time[cur_start+1:tm])
                else:
                    print('err')
        return out
    
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        # output
        out = [0] * n
        q = list()
        prv_time = -1
        for entry in logs:
            id, state, tm = entry.split(':')
            id, tm = int(id), int(tm)          
            if state=='start':
                if q:
                    out[q[-1]] += tm - prv_time
                q.append(id)
                prv_time = tm
            else:
                out[q[-1]] += tm - prv_time + 1
                q.pop()
                prv_time = tm+1                
        return out
    
    
msol = Solution()
n = 2
logs =   ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]
ares = msol.exclusiveTime(n, logs)
print(ares) 
    
                        
            