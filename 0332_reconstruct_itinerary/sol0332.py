'''
Created on Jan 9, 2021

@author: Q
'''
import copy

class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        N = len(tickets)+1
        d_tickets = dict()
        for s,t in tickets:
            if s in d_tickets:
                d_tickets[s].append(t)
            else:
                d_tickets[s] = [t]
            if t not in d_tickets:
                d_tickets[t] = []
        
        for s in d_tickets:
            d_tickets[s] = sorted(d_tickets[s])
        
        res = []
        ans = ['JFK']
        
        def add_to_itinerary(ans, all_tickets):
            cur_s = all_tickets[ans[-1]]
            if len(cur_s)==0:
                if len(ans)==N:
                    res.append(copy.deepcopy(ans))
                    return True                                        
            else:
                for i in range(len(cur_s)):
                    s = cur_s.pop(i)
                    ans.append(s)
                    if add_to_itinerary(ans, all_tickets):
                        return True
                    ans.pop()
                    cur_s.insert(i, s)
        
        add_to_itinerary(ans, d_tickets)        
        return res
    

msol = Solution()
input =  [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
ares = msol.findItinerary(input)
print(ares)   
        
        
        
        