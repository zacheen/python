# 3447. Assign Elements to Groups with Constraints
# https://leetcode.com/problems/assign-elements-to-groups-with-constraints/description/

from typing import List
from math import inf

from collections import defaultdict
# given ans : 1501ms Beats100.00%
# generating all the factors of every nums : O(nlogn)
# this part have to put outside, preventing recalculate
MAX = 10 ** 5 + 1
fac = [[] for _ in range(MAX)]
for i in range(1, MAX):
    for j in range(i, MAX, i):
        fac[j].append(i)

class Solution:
    def assignElements(self, a: List[int], b: List[int]) -> List[int]:
        n = len(a)
        m = len(b)
        res = [-1] * n
        pos = defaultdict(lambda: m)
        for i in range(m):
            pos[b[i]] = min(pos[b[i]], i)
        for i, num in enumerate(a):
            c = m
            for f in fac[num]:
                c = min(c, pos[f])
            if c != m:
                res[i] = c
        return res
    
# my after know how to calculate all factors : 1121ms Beats100.00%
class Solution:
    def assignElements(self, groups: List[int], elements: List[int]) -> List[int]:
        ans = []
        ele_to_i = {e:i for i, e in reversed(list(enumerate(elements)))}
        for g in groups :
            min_i = min(ele_to_i.get(f, inf) for f in fac[g])
            ans.append(-1 if min_i == inf else min_i)
        return ans
    
# my Time Limit Exceeded
# class Solution:
#     def assignElements(self, groups: List[int], elements: List[int]) -> List[int]:
#         ans = [-1]*len(groups)
#         not_seen = set(range(len(groups)))
#         for e_i , e in enumerate(elements) :
#             need_to_remove = []
#             for a_i in not_seen :
#                 if groups[a_i] % e == 0:
#                     ans[a_i] = e_i
#                     need_to_remove.append(a_i)
#             for a_i in need_to_remove :
#                 not_seen.remove(a_i)
#         return ans

s = Solution()
print("ans :",s.assignElements([8,4,3,2,4], [4,2])) # [0, 0, -1, 1, 0]
print("ans :",s.assignElements([2,3,5,7], [5,3,3])) # [-1, 1, 0, -1]



