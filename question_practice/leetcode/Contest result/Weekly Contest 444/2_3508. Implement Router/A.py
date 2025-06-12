# 3508. Implement Router
# https://leetcode.com/problems/implement-router/description/

from typing import List
from math import inf
from collections import defaultdict, deque
from sortedcontainers import SortedList

# my 577ms Beats31.42%
class Router:
    def __init__(self, memoryLimit: int):
        self.mem = deque()
        self.lim = memoryLimit
        self.dest_mem = defaultdict(SortedList)
    
    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        # check dup
        ret_i = self.dest_mem[destination].bisect_left((timestamp, source))
        if ret_i < len(self.dest_mem[destination]) and self.dest_mem[destination][ret_i] == (timestamp, source) :
            return False
        
        # add
        self.mem.append((source, destination, timestamp))
        self.dest_mem[destination].add( (timestamp, source) )

        # if exceed lim > remove
        if len(self.mem) > self.lim :
            source, destination, timestamp = self.mem.popleft()
            self.dest_mem[destination].remove( (timestamp, source) )
        return True

    def forwardPacket(self) -> List[int]:
        if len(self.mem) == 0 :
            return []
        source, destination, timestamp = self.mem.popleft()
        self.dest_mem[destination].remove( (timestamp, source) )
        return [source, destination, timestamp]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        ret_st = self.dest_mem[destination].bisect_left((startTime, -1))
        ret_end = self.dest_mem[destination].bisect_left((endTime, inf))
        return ret_end - ret_st



