# 304. Range Sum Query 2D - Immutable
# https://leetcode.com/problems/range-sum-query-2d-immutable/description/

from typing import List
import functools

# my 76ms Beats98.28%
from itertools import accumulate
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.sum_mem = []
        for i1, line in enumerate(matrix) :
            this_line = list(accumulate(line))
            if i1 > 0 :
                for i2, sum_up in enumerate(self.sum_mem[-1]) :
                    this_line[i2] += sum_up
            self.sum_mem.append(this_line)

    def get_sum(self, n1, n2):
        if n1<0 or n2<0 :
            return 0
        return self.sum_mem[n1][n2]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.get_sum(row2, col2) - self.get_sum(row1-1, col2) - self.get_sum(row2, col1-1) +self.get_sum(row1-1, col1-1) 

# given ans
# same concept, but mine implement method is better



