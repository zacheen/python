# 2327. Number of People Aware of a Secret
# https://leetcode.com/problems/number-of-people-aware-of-a-secret

from typing import List
from math import inf
from collections import deque

# my 2ms Beats94.89%
class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        delay_q = deque([0]*delay)
        delay_q[-1] = 1
        forget_q = deque([0]*forget-delay)
        active_p = 0
        for _i in range(n-1):
            active_p -= forget_q.popleft()
            new_p = delay_q.popleft()
            active_p += new_p
            delay_q.append(active_p)
            forget_q.append(new_p)
            # _ret = active_p + sum(delay_q)
            # _ = ""
        return (active_p + sum(delay_q)) % (10**9+7)

s = Solution()
print("ans :",s.peopleAwareOfSecret(n = 6, delay = 2, forget = 4)) # 5
print("ans :",s.peopleAwareOfSecret(n = 4, delay = 1, forget = 3)) # 6
# print("ans :",s.peopleAwareOfSecret()) # 



