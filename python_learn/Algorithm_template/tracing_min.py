# tracing min / trace min
    # 在 加入 跟 移除 的動作之後，依然可以找到最小值
# tracing max / trace max
    # 雖然是 tracing min，但是可以用負號來實現 tracing max

from collections import Counter
from heapq import heappop, heappush

# faster version, also easier to implement
class Trace_min_with_indx:
    def __init__(self):
        self.heap = []
        self.remove_count = Counter()
    
    def add(self, n, i):
        heappush(self.heap, (n,i))

    def min(self, i): # 剛好 i 會被保留
        while self.heap and self.heap[0][1] < i:
            heappop(self.heap)
        if self.heap:
            return self.heap[0][0]
        else :
            return 0

class Trace_min:
    def __init__(self):
        self.heap = []
        self.remove_count = Counter()
    
    def add(self, n):
        heappush(self.heap, n)

    def remove(self, n):
        self.remove_count[n] += 1

    def min(self):
        while self.heap and self.remove_count[self.heap[0]] > 0:
            self.remove_count[heappop(self.heap)] -= 1
        if self.heap:
            return self.heap[0]
        else :
            return 0

