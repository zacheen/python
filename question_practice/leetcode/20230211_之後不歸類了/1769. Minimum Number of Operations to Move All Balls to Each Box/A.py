# 1769. Minimum Number of Operations to Move All Balls to Each Box
# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/description

from typing import List
import functools

# my 4ms Beats97.07%
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        mem = [0]*len(boxes)
        now_m = int(boxes[0])
        for i in range(1,len(boxes)) :
            mem[i] = mem[i-1] + now_m
            if boxes[i] == "1" :
                now_m += 1
        
        mem_2 = 0
        now_m = int(boxes[-1])
        for i in range(len(boxes)-2,-1,-1) :
            mem_2 += now_m
            if boxes[i] == "1" :
                now_m += 1
            mem[i] += mem_2
        return mem

# given ans
# same

s = Solution()
print("ans :",s.minOperations(boxes = "001011")) # [11,8,5,4,3,4]



