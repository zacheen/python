import heapq
class TreeSet:
    def __init__(self):
        self.items = []
        self.items_set = set()

    def add(self, num: int):
        if num not in self.added_set :
            heapq.heappush(self.added, num)
            self.added_set.add(num)

    def pop(self) -> int:
        min = heapq.heappop(self.added)
        self.added_set.remove(min)
        return min

# 用法應該跟 sorted系列相同