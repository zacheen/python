# 1301. Number of Paths with Max Score
# https://leetcode.com/problems/number-of-paths-with-max-score/description/

from typing import List
from math import inf

# my 67ms Beats100.00%
MOD = 10**9+7
class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        mem = [[0,0] for _ in range(len(board))]
        for l in board :
            new_mem = []
            for n2, num in enumerate(l):
                if num == "E" :
                    new_mem.append([0,1])
                    continue
                elif num == "X" :
                    new_mem.append([0,0])
                    continue
                elif num == "S" :
                    num = 0
                # from up
                max_s, cou = mem[n2]
                if n2 != 0 :
                    # from top left
                    if mem[n2-1][0] > max_s :
                        max_s, cou = mem[n2-1]
                    elif mem[n2-1][0] == max_s :
                        cou += mem[n2-1][1]
                    # from left
                    if new_mem[n2-1][0] > max_s :
                        max_s, cou = new_mem[n2-1]
                    elif new_mem[n2-1][0] == max_s :
                        cou += new_mem[n2-1][1]
                max_s += int(num)
                new_mem.append([max_s, cou%MOD])
            mem = new_mem
        if mem[-1][1] == 0 :
            return [0,0]
        else :
            return mem[-1]

# given ans


s = Solution()
print("ans :",s.pathsWithMaxScore(["E23",
                                   "2X2",
                                   "12S"])) # [7,1]
print("ans :",s.pathsWithMaxScore(["E12",
                                   "1X1",
                                   "21S"])) # [4,2]
print("ans :",s.pathsWithMaxScore(["E11",
                                   "XXX",
                                   "11S"])) # [0,0]



