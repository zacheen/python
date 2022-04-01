# my Runtime: 1436 ms, faster than 17.42% of Python3
# O(nlogn) # 每次插入 O(logn) * n次
class MedianFinder:
    def __init__(self):
        self.arr = []

    def addNum(self, num: int):
        bisect.insort_right(self.arr, num)
        # self.arr.append(num)

    def findMedian(self):
        # print(self.arr)
        if len(self.arr) % 2 == 0 :
            mid_indx = len(self.arr)//2
            return (self.arr[mid_indx]+self.arr[mid_indx-1])/2
        else :
            return self.arr[len(self.arr)//2]

# given ans
# Runtime: 544 ms, faster than 93.70% of Python3 
# 奇怪 我感覺時間複雜度沒有差這麼多啊 ?
# O(nlogn)
class MedianFinder:
    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int):
        if not self.maxHeap or num <= -self.maxHeap[0]:
            heapq.heappush(self.maxHeap, -num)
        else:
            heapq.heappush(self.minHeap, num)

        # balance two heaps s.t.
        # |maxHeap| >= |minHeap| and |maxHeap| - |minHeap| <= 1
        # 不能要取的時候再平衡 要不然 maxHeap[0] 可能兩邊數量會很偏
        # 造成要取的時候 要一直搬移
        if len(self.maxHeap) < len(self.minHeap):
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
        elif len(self.maxHeap) - len(self.minHeap) > 1:
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))

    def findMedian(self):
        if len(self.maxHeap) == len(self.minHeap):
            return (-self.maxHeap[0] + self.minHeap[0]) / 2.0
        return -self.maxHeap[0]

s = Solution()
print(s.())



