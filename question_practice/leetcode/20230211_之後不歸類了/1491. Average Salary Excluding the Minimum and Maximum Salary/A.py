# 1491. Average Salary Excluding the Minimum and Maximum Salary
# https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/

from typing import List
import functools

# my
class Solution:
    def average(self, salary: List[int]) -> float:
        # v1
        # min_s = salary[0]
        # max_s = salary[0]
        # sum_s = 0
        # for s in salary :
        #     min_s = min(min_s, s)
        #     max_s = max(max_s, s)
        #     sum_s += s

        # v2
        min_s = min(salary)
        max_s = max(salary)  
        sum_s = sum(salary)  
        return (sum_s - min_s - max_s) / (len(salary)-2)

# # given ans
# # but I think sort is slower
# class Solution:
#     def average(self, salary: List[int]) -> float:
#         salary.sort()
#         return sum(salary[1:-1]) / (len(salary)-2)

s = Solution()
print(s.average())



