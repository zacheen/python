# 1396. Design Underground System
# https://leetcode.com/problems/design-underground-system/

from typing import List
import functools

from collections import defaultdict
from collections import Counter

# # my v1 Beats 28.23%
# class UndergroundSystem:
#     def __init__(self):
#         self.total_time = defaultdict(Counter)
#         self.total_count = defaultdict(Counter)
#         self.check_in_time = {}

#     def checkIn(self, id: int, stationName: str, t: int) -> None:
#         self.check_in_time[id] = (stationName, t)

#     def checkOut(self, id: int, stationName: str, t: int) -> None:
#         start_sta, start_time = self.check_in_time[id]
#         self.total_time[start_sta][stationName] += (t - start_time)
#         self.total_count[start_sta][stationName] += 1

#     def getAverageTime(self, startStation: str, endStation: str) -> float:
#         return self.total_time[startStation][endStation] / self.total_count[startStation][endStation]
    
# my v2 Beats 42.90%
class Cal_Average:
    def __init__(self):
        self.count = 0
        self.total_time = 0
        
    def new_record(self, t):
        self.total_time += t
        self.count += 1
    
    def cal_average(self):
        return self.total_time/self.count

class UndergroundSystem:
    def __init__(self):
        self.cal_ave = defaultdict(lambda: defaultdict(Cal_Average))
        self.check_in_time = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in_time[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_sta, start_time = self.check_in_time[id]
        self.cal_ave[start_sta][stationName].new_record(t - start_time)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.cal_ave[startStation][endStation].cal_average()

# given ans Beats 64.83%
# 我用 [startStation][endStation] 兩個key
# 他把 [(startStation, endStation)] 這樣當作一個key
class UndergroundSystem:
    def __init__(self):
        # {id: (stationName, time)}
        self.checkIns = {}
        # {route: (numTrips, totalTime)}
        self.checkOuts = defaultdict(lambda: [0, 0])

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkIns[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.checkIns.pop(id)
        route = (startStation, stationName)
        self.checkOuts[route][0] += 1
        self.checkOuts[route][1] += t - startTime

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        numTrips, totalTime = self.checkOuts[(startStation, endStation)]
        return totalTime / numTrips

# s = Solution()
# print(s.())



