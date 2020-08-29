'''
Created on Aug 29, 2020

@author: Q
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
         
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3, p = None, None
        p1, p2 = l1, l2
        carry = 0
        while (p1 != None) | (p2 != None):
            x1, x2 = 0, 0
            if p1 != None:
                x1 = int(p1.val)
            if p2 != None:
                x2 = int(p2.val)
            x3 = x1 + x2 + carry
            if l3:
                p.next = ListNode(x3 % 10) 
                p = p.next               
            else:    
                l3 = ListNode(x3 % 10)
                p = l3
            #print(l1.val)
            #print(l2.val)
            #print(p.val)            
            carry = int(x3 / 10)            
            if p1 != None: p1 = p1.next
            if p2 != None: p2 = p2.next
        if carry==1:
            p.next = ListNode(carry)
        return l3


in1 = ListNode(2)
p1 = in1
for i in [4,3]:
    p1.next = ListNode(i)
    p1 = p1.next
    
in2 = ListNode(5)
p1 = in2
for i in [6,4]:
    p1.next = ListNode(i)
    p1 = p1.next

msol = Solution()
out1 = msol.addTwoNumbers(in1, in2)
p2 = out1
while p2:
    print(p2.val)    
    p2 = p2.next
    
p2 = in1
while p2:
    print(p2.val)    
    p2 = p2.next    