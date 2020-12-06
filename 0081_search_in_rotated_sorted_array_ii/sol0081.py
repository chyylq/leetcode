'''
Created on Dec 6, 2020

@author: Q

binary search
mid = [(head+tail)/2]
compare the target with the head and mid
if head=target or mid=target, found
elif head<target<mid, it is in the first half, search in (head+1, mid-1) if head+1<=mid-1
compare the target with mid and tail
if mid=target or tail=target, found
elif target<tail or mid<target, it is in the second half, search in (mid+1, tail-1) if mid+1<=tail-1
'''
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        def binary(n, head, tail, val):
            mid = int(float(head+tail) / 2)            
            if val in (n[head],n[mid],n[tail]): return True
            else:
                r1, r2 = False, False
                if n[head]<val or val<n[mid]:
                    if head+1<=mid-1:
                        r1 = binary(n,head+1,mid-1,val)                
                if val<n[tail] or n[mid]<val:
                    if mid+1<=tail-1:
                        r2 = binary(n,mid+1,tail-1,val)
                return r1 | r2                
            
        head = 0
        tail = len(nums)-1
        if head<=tail:
            return binary(nums, head, tail, target)
        else:
            return False
    
msol = Solution()
nums = [1,1,1,3,1]
target = 3
ares = msol.search(nums, target)
print(ares)
        