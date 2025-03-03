# 3186. Maximum Total Damage With Spell Casting
# https://leetcode.com/problems/maximum-total-damage-with-spell-casting/description/

from typing import List
from math import inf
from collections import Counter, deque

# my 440ms Beats72.19%
    # mine is slower, because my dp_q is 2D array
    # but this method saves more space
class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        cou = Counter(power)
        nums = list(cou.keys())
        nums.sort()

        dp_q = deque([]) # dp_q[i] = [last_num, sum]
        for n in nums :
            max_s = 0
            for i in range(len(dp_q)-1,-1,-1) :
                prev_n, prev_s = dp_q[i]
                if prev_n+2 < n :
                    max_s = prev_s
                    break
            max_s += n*cou[n]
            if not dp_q or max_s > dp_q[-1][1] :
                dp_q.append((n, max_s))
                if len(dp_q) > 3 :
                    dp_q.popleft()
        return dp_q[-1][-1]

# given ans 318ms Beats96.88%
class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        count = Counter(power)
        arr = [0, 0, 0] + sorted(list(count.keys()))
        n = len(arr)
        dp = [0] * n
        
        for i in range(3, n):
            if arr[i] - arr[i - 1] > 2:
                dp[i] = dp[i - 1] + count[arr[i]] * arr[i]
            elif arr[i] - arr[i - 2] > 2:
                dp[i] = max(dp[i - 1], dp[i - 2] + count[arr[i]] * arr[i])
            else:
                dp[i] = max(dp[i - 1], dp[i - 3] + count[arr[i]] * arr[i])
        
        return dp[-1]
    


s = Solution()
print("ans :",s.maximumTotalDamage([1,1,3,4])) # 6
print("ans :",s.maximumTotalDamage([7,1,6,6])) # 13
print("ans :",s.maximumTotalDamage([1,3,6,7])) # 10
print("ans :",s.maximumTotalDamage([2,1,4,3,1,1,1,5])) # 9



