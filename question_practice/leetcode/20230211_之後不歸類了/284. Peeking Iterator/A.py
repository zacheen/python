# my 
class PeekingIterator:
    def __init__(self, iterator):
        self.now_indx = 0
        self.mem = []
        while iterator.hasNext() :
            self.mem.append(iterator.next())
        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.mem[self.now_indx]
        

    def next(self):
        """
        :rtype: int
        """
        ret = self.mem[self.now_indx]
        self.now_indx += 1
        return ret

        

    def hasNext(self):
        """
        :rtype: bool
        """

        # return (self.now_indx + 1) <= len(self.mem)
        return self.now_indx < len(self.mem)

# given ans # Beats 73.99%
# 想法是直接先把這一個取出來
class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self.buffer = self.iterator.next() if self.iterator.hasNext() else None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        """
        return self.buffer

    def next(self):
        next = self.buffer
        self.buffer = self.iterator.next() if self.iterator.hasNext() else None
        return next

    def hasNext(self):
        return self.buffer is not None




