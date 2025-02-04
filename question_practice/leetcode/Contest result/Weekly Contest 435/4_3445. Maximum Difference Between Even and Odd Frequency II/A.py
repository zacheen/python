# 3445. Maximum Difference Between Even and Odd Frequency II
# https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-ii/description/

from typing import List
import functools

from math import inf
from collections import deque
# my 4039ms Beats100.00%
class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        s = [int(c) for c in s]
        def max_diff(n1,n2):
            stack_to_add = deque([[None,[]] for _ in range(k-1)])
            k_limit = k - 1
            min_diff = [[[0,0]],[],[],[]] # [diff,n2_cou]
            # [n1%2*2+n2%2] # [n1_even_n2_even, n1_even_n2_odd, n1_odd_n2_even, n1_odd_n2_odd]
            cou = [0]*5
            max_ret = -inf
            for indx, n in enumerate(s) :
                cou[n] += 1
                now_diff = cou[n1]-cou[n2]
                state = cou[n1]%2*2+cou[n2]%2
                # update max_ret
                if indx >= k_limit and cou[n1] != 0 and cou[n2] != 0 :
                    for di, co in min_diff[(state+2)%4] :
                        if cou[n2] - co != 0 :
                            max_ret = max(max_ret, now_diff - di)
                # stack
                stack_to_add.append((state, (now_diff, cou[n2])))
                # update min_diff
                state, info = stack_to_add.popleft()
                if state != None :
                    state_mem = min_diff[state]
                    state_mem.append(info)
                    for i in range(len(state_mem)-1, 0, -1):
                        if state_mem[i][0] < state_mem[i-1][0] :
                            state_mem[i],state_mem[i-1] = state_mem[i-1], state_mem[i]
                    if len(state_mem) >= 3:
                        state_mem.pop()
            return max_ret

        return max(max_diff(n1,n2) for n1 in range(5) for n2 in range(5) if n1 != n2)

from collections import defaultdict
# given ans : 3530ms Beats100.00%
# same concept, but optimized
    # 1. using (odd or even, odd or even) as state too simplify
    # 2. while ii <= i-k+1 and pa[ii] < pa[-1] and pb[ii] < pb[-1]:
        # 通過了 我才加入可以判斷的list中 其他存在stack裡面 或用indx標記 
class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        ans = -inf
        for a in "01234": 
            for b in "01234": 
                if a != b: 
                    seen = defaultdict(lambda : inf)
                    pa = [0]
                    pb = [0]
                    ii = 0 
                    for i, ch in enumerate(s): 
                        pa.append(pa[-1])
                        pb.append(pb[-1])
                        if ch == a: pa[-1] += 1
                        elif ch == b: pb[-1] += 1
                        while ii <= i-k+1 and pa[ii] < pa[-1] and pb[ii] < pb[-1]: 
                            key = (pa[ii] % 2, pb[ii] % 2) 
                            diff = pa[ii] - pb[ii]
                            seen[key] = min(seen[key], diff)
                            ii += 1
                        key = (1 - pa[-1] % 2, pb[-1] % 2) 
                        diff = pa[-1] - pb[-1]
                        ans = max(ans, diff - seen[key])
        return ans 

s = Solution()
print("ans :",s.maxDifference(s = "12233", k = 4)) # -1
print("ans :",s.maxDifference(s = "1122211", k = 3)) # 1
print("ans :",s.maxDifference(s = "110", k = 3)) # -1
print("ans :",s.maxDifference(s = "11131340", k = 8)) # -1
print("ans :",s.maxDifference(s = "111320214", k = 9)) # -1
print("ans :",s.maxDifference(s = "44114402", k = 7)) # 1



