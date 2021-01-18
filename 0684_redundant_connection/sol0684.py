'''
Created on Jan 18, 2021

@author: Q

union set class
'''
class UF():
    def __init__(self, n):
        self.count=n
        self.parent=[x for x in range(n+1)]
        self.size=[0 for _ in range(n+1)]
        
    def union(self, u, v):
        parent_u = self.find(u)
        parent_v = self.find(v)
        if parent_u == parent_v:
            return
        elif self.size[parent_u]<self.size[parent_v]:
            self.parent[parent_u] = parent_v
            self.size[parent_v] += self.size[parent_u]
        else:
            self.parent[parent_v] = parent_u
            self.size[parent_u] += self.size[parent_v]
        self.count -= 1
        
    def find(self, p):
        # find the root of p by continuously looking till a node is pointing to itself
        # while searching, flatter the chain so next time, find will be fast as only common root matters
        while (self.parent[p] != p):
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p
            
    def connected(self, p, q):
        return self.find(p) == self.find(q)
        
    
class Solution(object):    
    
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        n_nodes = max([max(u,v) for u,v in edges])
        uf = UF(n_nodes)
        for u,v in edges:
            if uf.connected(u,v):
                return (u,v)
            else:
                uf.union(u,v)
        return (-1,-1)

msol = Solution()
courses =  [[1,2], [2,3], [3,4], [1,4], [1,5]]
ares = msol.findRedundantConnection(courses)
print(ares) 
            
            