'''
Created on Sep 5, 2020

@author: Q
'''
import math
import copy

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def merge_2_lists(l1, l2):
            head = ListNode()
            l = head
            tail = l            
            while (l1 or l2):
                if l1 and l2:
                    if l1.val < l2.val:
                        l.next = l1
                        l1 = l1.next
                    else:
                        l.next = l2
                        l2 = l2.next
                elif l1:
                    l.next = l1
                    l1 = l1.next
                else:
                    l.next = l2
                    l2 = l2.next
                l = l.next
                tail = l                
            return head.next, tail
                            
        def merge(head, step):
            l_head_prv = head
            l = head.next           
            while (l):
                head1, head2 = ListNode(), ListNode()
                l1 = head1
                l2 = head2 
                for i in range(step):
                    if l:
                        l1.next = l 
                        l = l.next              
                        l1 = l1.next                    
                l1.next = None
                for i in range(step):
                    if l:
                        l2.next = l 
                        l = l.next                        
                        l2 = l2.next               
                l2.next = None
                l_head, l_tail = merge_2_lists(head1.next, head2.next)
                l_head_prv.next = l_head
                l_tail.next = l
                l_head_prv = l_tail
        
        n_len = 0
        head0 = ListNode()
        head0.next = head
        l = head0.next
        while (l):
            n_len += 1
            l = l.next
        if n_len==0: return head
        for i in range(int(math.ceil(math.log(n_len,2)))):
            step = int(math.pow(2,i))
            merge(head0, step)        
        return head0.next
    
    
hd = ListNode(4)
l = hd
l.next = ListNode(2)
l = l.next
l.next = ListNode(1)
l = l.next
l.next = ListNode(3)
#l = l.next
#l.next = ListNode(-1)
l = hd
while (l):
    print(l.val)
    l = l.next

l = hd
msol = Solution()
hd1 = msol.sortList(hd)
l = hd1
while (l):
    print(l.val)
    l = l.next

 