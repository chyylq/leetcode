'''
Created on Jan 24, 2021

@author: Q
'''
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self._x = []
        self.i = 0
        
        def iterate_list(nestedList):
            for x in nestedList:
                if x.isInteger():
                    self._x.append(x.getInteger())
                else:
                    iterate_list(x.getList())
        iterate_list(nestedList)
        
    def next(self):
        """
        :rtype: int
        """
        self.i += 1  
        return self._x[self.i]
                
    def hasNext(self):
        """
        :rtype: bool
        """
        if self.i+1<len(self._x):
            return True
        