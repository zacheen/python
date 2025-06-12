# 3458. Select K Disjoint Special Substrings
# https://leetcode.com/problems/select-k-disjoint-special-substrings/description/

from typing import List
from math import inf
from functools import cache

# given ans
class Solution:
    def maxSubstringLength(self, s: str, k: int) -> bool:
        len_s = len(s)
        end_i = len_s-1
        c_range = {}  # start end
        for i, c in enumerate(s):
            c_range.setdefault(c, [i, i])
            c_range[c][1] = i

        intervals = []
        for start, end in c_range.values():
            i = start
            while i <= end:
                new_st, new_en = c_range[s[i]]
                if new_en > end:
                    end = new_en
                if new_st < start:
                    break
                i += 1
            if start != 0 or end != end_i:
                intervals.append([start, end])
        
        intervals.sort(key=lambda e: e[1])
        ans = 0
        floor = -5
        for start, end in intervals:
            if start > floor:
                floor = end
                ans += 1
        return ans >= k

# my 1178ms Beats28.88%
class Solution:
    def maxSubstringLength(self, s: str, k: int) -> bool:
        have_pre = [False]*len(s)
        seen = {}
        next_indx = {}
        for i,c in enumerate(s) :
            if c in seen :
                next_indx[seen[c]] = i
                have_pre[i] = True
            seen[c] = i
        
        @cache
        def find_end(now_i): 
            l = now_i
            r = next_indx.get(now_i, l)
            for mid_i in range(l+1, r+1): # actually O(n)
                new_r = find_end(mid_i)
                if new_r > r :
                    r = new_r
                    have_pre[mid_i] = True
            return r

        stack_end = []
        last_i = len(s)-1
        for st in range(len(s)): # O(n)
            if have_pre[st] :
                continue
            end_r = find_end(st)
            # actually O(n), because at most append len(n) times
            while stack_end and end_r < stack_end[-1] :
                stack_end.pop()
            if len(stack_end) == 0 or end_r > stack_end[-1] :
                if end_r == last_i and st == 0 : continue
                stack_end.append(end_r)
        return len(stack_end) >= k



s = Solution()
# print("ans :",s.maxSubstringLength(s = "abcdbaefab", k = 2)) # T
# print("ans :",s.maxSubstringLength(s = "cdefdc", k = 3)) # F
print("ans :",s.maxSubstringLength(s = "wxcjhhcjrpfbdiljnvqxwkfqzobymjhtncogexchzhmdpuzyiqxcnrrteuzt", k = 7)) # F



