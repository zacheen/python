# 1700. Number of Students Unable to Eat Lunch
# https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/description/

from typing import List
from math import inf
from collections import Counter

# my v1
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        cnt_stu = Counter(students)
        
        # print(find, num)
        for i, n in enumerate(sandwiches):
            if cnt_stu[n] > 0 :
                cnt_stu[n] -= 1
            else :
                return len(students) - i
        return 0
            

s = Solution()
print("ans :",s.countStudents(students = [1,1,0,0], sandwiches = [0,1,0,1])) # 
print("ans :",s.countStudents(students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1])) # 



