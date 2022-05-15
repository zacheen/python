# my 
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        # flatten
        self.flat_list = self.flatten(nestedList)
            
    def flatten(self,nest):
        if type(nest) != type([]) :
            if nest.isInteger() :
                return [nest.getInteger()]
            else :
                return self.flatten(nest.getList())
        else :
            ret = []
            for i in nest :
                ret += self.flatten(i)
            return ret
    
    def next(self):
        return self.flat_list.pop(0)
    
    def hasNext(self):
        return self.flat_list

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

# given ans
# 我是 回傳list 但其實可以找到數字就直接加到最尾端
# flatten 有做優化
class NestedIterator:
    def __init__(self, nestedList: List[NestedInteger]):
        self.q = deque()
        self.addInteger(nestedList)

    def next(self):
        return self.q.popleft()

    def hasNext(self):
        return self.q

    def addInteger(self, nestedList: List[NestedInteger]):
        for ni in nestedList:
            if ni.isInteger():
                self.q.append(ni.getInteger())
            else:
                self.addInteger(ni.getList())



