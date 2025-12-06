# 3709. Design Exam Scores Tracker
# https://leetcode.com/problems/design-exam-scores-tracker/description/

from typing import List
from math import inf
from bisect import bisect_left, bisect_right

# my optimized v2 215ms Beats59.71%
class ExamTracker:
    def __init__(self):
        self.time = [-1]
        self.total_score = [0]

    def record(self, time: int, score: int) -> None:
        self.time.append(time)
        self.total_score.append(self.total_score[-1] + score)

    def totalScore(self, startTime: int, endTime: int) -> int:
        li = bisect_left(self.time, startTime)-1
        ri = bisect_right(self.time, endTime)-1
        # print(li, ri)
        return self.total_score[ri] - self.total_score[li]


# my v1 252ms Beats41.87%
class ExamTracker:
    def __init__(self):
        self.mem = [(-1,0)]

    def record(self, time: int, score: int) -> None:
        self.mem.append( (time, self.mem[-1][1] + score) )

    def totalScore(self, startTime: int, endTime: int) -> int:
        li = bisect_left(self.mem, (startTime, 0))-1
        ri = bisect_right(self.mem, (endTime, inf))-1
        return self.mem[ri][1] - self.mem[li][1]

# Your ExamTracker object will be instantiated and called as such:
# obj = ExamTracker()
# obj.record(time,score)
# param_2 = obj.totalScore(startTime,endTime)

