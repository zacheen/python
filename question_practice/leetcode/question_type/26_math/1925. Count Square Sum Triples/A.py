# 1925. Count Square Sum Triples
# https://leetcode.com/problems/count-square-sum-triples

from typing import List
from math import inf
from bisect import bisect_left
from functools import cache

# my : 0ms
all_pos_l = list(i**2 for i in range(1,251))
all_pos_s = set(all_pos_l)
@cache
def dp_countTriples(n):
    if n <= 1 :
        return 0
    
    prev_cnt = dp_countTriples(n-1)
    c_squ = all_pos_l[n]
    half_c_squ = c_squ//2
    # because of square, half_c_squ~c_squ is much sparser than 0~half_c_squ
    st_i = bisect_left(all_pos_l, half_c_squ)
    for b_squ in all_pos_l[st_i:n] :
        if (c_squ-b_squ) in all_pos_s :
            # print(c_squ, b_squ, c_squ-b_squ)
            prev_cnt += 1
    return prev_cnt


class Solution:
    def countTriples(self, n: int) -> int:
        # assume a < b, and later *2
        # and there is no situation that a == b
        return dp_countTriples(n-1)*2

s = Solution()
print("ans :",s.countTriples(5)) # 2
print("ans :",s.countTriples(10)) # 4
print("ans :",s.countTriples(1)) # 0



