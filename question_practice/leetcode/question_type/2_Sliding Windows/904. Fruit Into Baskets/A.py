# 904. Fruit Into Baskets
# https://leetcode.com/problems/fruit-into-baskets

from typing import List
from math import inf
from collections import deque

# my 31ms Beats99.55%
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        now_pick = {fruits[0]}
        now_pick_f = 0
        last_seen = fruits[0]
        last_seen_f = 0
        max_ans = 0
        for i, f in enumerate(fruits) :
            if f not in now_pick :
                if (new_l := i - now_pick_f) > max_ans :
                    max_ans = new_l
                now_pick = {f, last_seen}
                now_pick_f = last_seen_f
            if f != last_seen :
                last_seen = f
                last_seen_f = i
        if (new_l := len(fruits) - now_pick_f) > max_ans :
            max_ans = new_l
        return max_ans

# given ans : shorter but slower
class Solution:
    def totalFruit(self, tree):
        count, i = {}, 0
        for j, v in enumerate(tree):
            count[v] = count.get(v, 0) + 1
            if len(count) > 2:
                count[tree[i]] -= 1
                if count[tree[i]] == 0: del count[tree[i]]
                i += 1
        return j - i + 1

s = Solution()
print("ans :",s.totalFruit([1,2,1])) # 3
print("ans :",s.totalFruit([0,1,2,2])) # 3
print("ans :",s.totalFruit([1,2,3,2,2])) # 4
print("ans :",s.totalFruit([3,3,3,1,2,1,1,2,3,3,4])) # 5
print("ans :",s.totalFruit([1,2,1,4,4,4])) # 4