# https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/description/

from typing import List
import functools

# my method 2 : 0ms Beats 100.00%
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        W_count = blocks[:k].count("W") # W_count 就是要修改的數量 == ans
        max_W_count = W_count # k長度中 字數重複最多的
        # for era, add in zip(blocks[:-k], blocks[k:]) :
        for indx in range(len(blocks)-k):
            era, add = blocks[indx], blocks[indx+k]
            # print(era, add)
            if add == "W" :
                W_count += 1
            if era == "W" :
                W_count -= 1
            
            max_W_count = min(max_W_count, W_count)

        ans = max(0, max_W_count)
        return ans

# # my method 1
# class Solution:
#     def minimumRecolors(self, blocks: str, k: int) -> int:
#         max_count = 0 # k長度中 字數重複最多的
#         W_count = 0
#         for indx, each_W in enumerate(blocks) :
#             if each_W == "W" :
#                 W_count += 1
            
#             if not indx < k :
#                 print(indx, blocks[indx-k])
#                 if blocks[indx-k] == "W" :
#                     W_count -= 1

#             if indx >= k-1 :
#                 print(W_count)
#                 max_count = max(max_count, k - W_count)

#         ans = max(0, k-max_count)
#         return ans

# given ans
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        countB = 0
        maxCountB = 0

        for i, block in enumerate(blocks):
            if block == 'B':
                countB += 1
            if i >= k and blocks[i - k] == 'B':
                countB -= 1
            maxCountB = max(maxCountB, countB)

        return k - maxCountB

s = Solution()
print("ans :",s.minimumRecolors(blocks = "WWWWWW", k = 4))
print("ans :",s.minimumRecolors(blocks = "WWWWBBWWW", k = 5))
print("ans :",s.minimumRecolors(blocks = "WWWBBWWWW", k = 5))
print("ans :",s.minimumRecolors(blocks = "WBBWWBBWBW", k = 7)) # 3
print("ans :",s.minimumRecolors(blocks = "WBWBBBW", k = 2)) # 0



