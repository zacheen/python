# 2038. Remove Colored Pieces if Both Neighbors are the Same Color
# https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/description/

from typing import List
import functools

# my 87ms Beats91.17%
class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        prev_c = "A"
        cou = cou_A = cou_B = 0
        for c in colors + "|" :
            if c == prev_c :
                cou += 1
            else :
                if prev_c == "A" : 
                    cou_A += max(0, cou-2)
                else :
                    cou_B += max(0, cou-2)
                
                prev_c = c
                cou = 1
        # print(cou_A , cou_B)
        return cou_A > cou_B

# given ans
# same concept

s = Solution()
print("ans :",s.winnerOfGame()) # 



