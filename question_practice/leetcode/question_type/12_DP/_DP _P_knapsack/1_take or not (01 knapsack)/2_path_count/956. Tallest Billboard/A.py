# 956. Tallest Billboard
# https://leetcode.com/problems/tallest-billboard

from typing import List
from math import inf
from collections import defaultdict

# my modify template knapsack_01_max_cnt : 268ms Beats85.91%
    # 追蹤每個點 最大可能的總和
    # 每個 rods 有可能是 1.正的 2.負的 3.不取
    # 當有和為0時 代表 正的總和 與 負的總和 相等 > 兩條鐵軌
class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        total_s = sum(rods)
        max_target = total_s//2
        
        mem = defaultdict(int)
        mem[0] = 0
        for num in rods:
            for s, max_sum in mem.copy().items() :
                new_max_sum = max_sum+num
                # pos
                if -max_target <= (new_s := s+num) <= max_target :
                    if new_max_sum > mem[new_s] :
                        mem[new_s] = new_max_sum
                # neg
                if -max_target <= (new_s := s-num) <= max_target :
                    if new_max_sum > mem[new_s] :
                        mem[new_s] = new_max_sum
        return mem[0]//2
    
# given ans optimized
    # like two sum : seperate into two part and try to find same sum

s = Solution()
print("ans :",s.tallestBillboard([1,2,3,6])) # 6
print("ans :",s.tallestBillboard([1,2,3,4,5,6])) # 10
print("ans :",s.tallestBillboard([1,2])) # 0



