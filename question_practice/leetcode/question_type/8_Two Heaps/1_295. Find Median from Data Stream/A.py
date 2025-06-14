# 295. Find Median from Data Stream
# https://leetcode.com/problems/find-median-from-data-stream/

# my practice again : 112ms Beats90.07%
from heapq import heappushpop, heappush
class MedianFinder:
    def __init__(self):
        self.heap1 = []
        self.heap2 = []

    def addNum(self, num: int) -> None:
        if len(self.heap1) > len(self.heap2) :
            # need to put into heap2
            if self.heap1 and num > self.heap1[0] :
                num = heappushpop(self.heap1, num)
            heappush(self.heap2, -num)
        else :
            # need to put into heap1
            if self.heap2 and num < -self.heap2[0] :
                num = -heappushpop(self.heap2, -num)
            heappush(self.heap1, num)

    def findMedian(self) -> float:
        if len(self.heap1) == len(self.heap2) :
            return (self.heap1[0] - self.heap2[0])/2
        else :
            return self.heap1[0]
