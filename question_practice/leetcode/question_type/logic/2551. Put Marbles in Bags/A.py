# 2551. Put Marbles in Bags
# https://leetcode.com/problems/put-marbles-in-bags

from typing import List
from math import inf
from itertools import pairwise

# my v2 optimized : 112ms Beats99.59%
class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        # 推理
        # 最左邊 跟 最右邊 一定會有
        # 其他的總和就是, 逗點的左右兩邊的數字
        # > sort 全部逗點的左右兩邊的數字

        len_p = len(weights)-1
        sum_end = k-1
        # print("init", sum_end)
        if sum_end > len_p<<1 :
            sum_end = len_p-sum_end
        # print(sum_end)
        if sum_end == 0 : return 0

        all_pair = [w1+w2 for w1,w2 in pairwise(weights)]
        all_pair.sort()
        return sum(all_pair[-sum_end:]) - sum(all_pair[:sum_end])

# my v1 120ms Beats92.56%
class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        # 推理
        # 最左邊 跟 最右邊 一定會有
        # 其他的總和就是, 逗點的左右兩邊的數字
        # > sort 全部逗點的左右兩邊的數字

        if k == 1 : return 0

        all_pair = [w1+w2 for w1,w2 in pairwise(weights)]
        all_pair.sort()
        return sum(all_pair[-(k-1):]) - sum(all_pair[:k-1])

s = Solution()
print("ans :",s.putMarbles(weights = [1,3,5,1], k = 2)) # 4
print("ans :",s.putMarbles(weights = [1, 3], k = 2)) # 0
print("ans :",s.putMarbles(weights = [1,4,2,5,2], k = 3)) # 0

# special testcase
print("ans :",s.putMarbles([25,74,16,5], 1)) # 0



