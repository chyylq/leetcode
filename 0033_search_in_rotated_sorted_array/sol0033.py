'''
Created on Dec 6, 2020

@author: Q
'''
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def binary(n, head, tail, val):
            if head>tail:
                return -1
            mid = int(float(head+tail) / 2)            
            if val==n[mid]: return mid
            else:         
                if n[head]<=n[mid]:  # 1st half sorted, 2nd half rotation                       
                    if n[head]<=val<n[mid]:                           
                        return binary(n,head,mid-1,val)
                    else:
                        return binary(n,mid+1,tail,val)
                else: # 1st half rotation, 2nd half sorted
                    if n[mid]<val<=n[tail]:                    
                        return binary(n,mid+1,tail,val)
                    else:
                        return binary(n,head,mid-1,val)                
            
        head = 0
        tail = len(nums)-1
        if head<=tail:
            return binary(nums, head, tail, target)
        else:
            return -1

msol = Solution()
nums = [3,1]
target = 1
ares = msol.search(nums, target)
print(ares)