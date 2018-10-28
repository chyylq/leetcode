# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 10:03:07 2018

object is a dictinary
the value is an object that is a double linked list with value in it
head node next point to the start of the linked list
tail node previous point to the end of the linked list
so every time the node is visited it is moved to the start
the end will be the one that is least recent visited and can be dropped
***create head and tail like normal nodes so don't worry about none pointer among normal node
get:
if exists in dict, get the node, remove the node, add the node (always in start)
put:
if exists in dict or not but capacity, get the node, remove the node, delete the node
create the node, add the node

add:
node next to head next (which can be tail in a single case)
head next's previous to node
head next to the node
node previous to the head

remove:
node previous to tail prev (which can be head)
tail prev's next to node
tail previous to the noe
node next to tail     
@author: yilin
"""

class LRUCache:
    
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.val =  value
            self.prv = None
            self.nxt = None
            
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.size = 0
        self.capacity = capacity
        self.head = self.Node(0,0)
        self.tail = self.Node(0,0)
        self.head.nxt = self.tail
        self.tail.prv = self.head
        self.dic = dict()
    
    def _add(self, node):
        node.nxt = self.head.nxt
        self.head.nxt.prv = node
        node.prv = self.head
        self.head.nxt = node
    
    def _remove(self, node):
        node.prv.nxt = node.nxt
        node.nxt.prv = node.prv
    
    def print(self):
        cur = self.head
        s = []
        while cur is not None:
            s.append((cur.key, cur.val))
            cur = cur.nxt            
        print (s)
                
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dic:
            node = self.dic[key]
            self._remove(node)
            self._add(node)
            #self.print()
            return node.val
        else:
            return -1
        
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        node = None
        if (key in self.dic):
            node = self.dic[key]
        elif (self.size>0) and (self.size==self.capacity):
            node = self.tail.prv
        if node is not None:
            self._remove(node)
            self.dic.pop(node.key)
            del node
            self.size = self.size - 1
        node_new = self.Node(key, value)
        self.dic[key] = node_new
        self._add(node_new)
        self.size = self.size + 1
        #self.print()
                

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
cache = LRUCache(2);

cache.put(1, 1);
cache.put(2, 2);
print(cache.get(1))       #returns 1
cache.put(3, 3);    #evicts key 2
print(cache.get(2))       #returns -1 (not found)
cache.put(4, 4);    #evicts key 1
print(cache.get(1))       #returns -1 (not found)
print(cache.get(3))       #returns 3
print(cache.get(4))       #returns 4        
'''
#["LRUCache","put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"]
#[[10],[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],
#[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],
cache = LRUCache(10)
cache.put(10, 13)
cache.put(3, 17)
cache.put(6, 11)
cache.put(10, 5)
cache.put(9, 10)
cache.get(13)
cache.put(2,19)
cache.get(2)
cache.get(3)
cache.put(5,25)
cache.get(8)
cache.put(9,22)
cache.put(5,5)
cache.put(1,30)
cache.get(11)
cache.put(9,12)
cache.get(7)
cache.get(5)
cache.get(8)
cache.get(9)
cache.put(4,30)
cache.put(9,3)
cache.get(9)
cache.get(10)
cache.get(10)
cache.put(6,14)
cache.put(3,1)
print('cache.get(3)', cache.get(3))
cache.put(10,11)
cache.get(8)
cache.put(2,14)
cache.get(1)
cache.get(5)
#[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],
#[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],        
cache.get(4)
cache.put(11,4)
cache.put(12,24)
cache.put(5,18)
cache.get(13)
cache.put(7,23)
cache.get(8)
cache.get(12)
cache.put(3,27)
cache.put(2,12)
cache.get(5)
cache.put(2,9)
cache.put(13,4)
cache.put(8,18)
cache.put(1,7)
cache.get(6)
cache.put(9,29)
cache.put(8,21)
cache.get(5)
cache.put(6,30)
cache.put(1,12)
cache.get(10)
cache.put(4,15)
cache.put(7,22)
cache.put(11,26)
cache.put(8,17)
cache.put(9,29)
cache.get(5)
cache.put(3,4)
cache.put(11,30)
cache.get(12)
cache.put(4,29)
print('cache.get(3)', cache.get(3))
#[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],
#[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]
cache.get(9)
cache.get(6)
cache.put(3,4)
cache.get(1)
cache.get(10)
cache.put(3,29)
cache.put(10,28)
cache.put(1,20)
cache.put(11,13)
cache.get(3)
cache.put(3,12)
cache.put(3,8)
cache.put(10,9)
cache.put(3,26)
cache.get(8)
cache.get(7)
cache.get(5)
cache.put(13,17)
cache.put(2,27)
'''
