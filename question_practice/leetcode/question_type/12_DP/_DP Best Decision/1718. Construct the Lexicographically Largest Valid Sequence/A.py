# 1718. Construct the Lexicographically Largest Valid Sequence
# https://leetcode.com/problems/construct-the-lexicographically-largest-valid-sequence

from typing import List
from math import inf

from sortedcontainers import SortedList, SortedSet # check which one is faster
# my 12ms Beats12.50%
# class Solution:
#     def constructDistancedSequence(self, n: int) -> List[int]:
#         ans = [0]*(2*n-1)
#         not_use = SortedList(range(n,0,-1))
#         def dfs():
#             nonlocal not_use
#             first_zero = n
#             for i, num in enumerate(ans) :
#                 if num == 0 :
#                     first_zero = i
#                     break
#             if first_zero == n :
#                 return True
#             for poss in not_use[::-1] :
#                 if poss == 1:
#                     ans[first_zero] = poss
#                     not_use.remove(poss)
#                     if dfs() :
#                         return True
#                     not_use.add(poss)
#                     ans[first_zero] = 0
#                 else :
#                     sec_pos = first_zero+poss
#                     if sec_pos < len(ans) and ans[sec_pos] == 0 :
#                         ans[first_zero] = poss
#                         ans[sec_pos] = poss
#                         not_use.remove(poss)
#                         if dfs() :
#                             return True
#                         not_use.add(poss)
#                         ans[first_zero] = 0
#                         ans[sec_pos] = 0
#             return False
#         dfs()
#         return ans

# optimized by given ans : 3ms Beats95.59%
# 1. passing indx, so each round don't have to find first_zero
# 2. use range big to small and check seen
class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        ans = [0]*(2*n-1)
        seen = set()
        def dfs(first_zero):
            # finding first_zero
            while first_zero < len(ans) :
                if ans[first_zero] != 0 :
                    first_zero += 1
                else :
                    break
            if first_zero == len(ans) :
                return True
            # dfs part
            nonlocal seen
            for poss in range(n,0,-1) :
                if poss in seen : continue
                if poss == 1:
                    ans[first_zero] = poss
                    seen.add(poss)
                    if dfs(first_zero+1) :
                        return True
                    seen.remove(poss)
                    ans[first_zero] = 0
                else :
                    sec_pos = first_zero+poss
                    if sec_pos < len(ans) and ans[sec_pos] == 0 :
                        ans[first_zero] = poss
                        ans[sec_pos] = poss
                        seen.add(poss)
                        if dfs(first_zero+1) :
                            return True
                        seen.remove(poss)
                        ans[first_zero] = 0
                        ans[sec_pos] = 0
            return False
        dfs(0)
        return ans


s = Solution()
# print("ans :",s.constructDistancedSequence(3)) # [3,1,2,3,2]
print("ans :",s.constructDistancedSequence(5)) # [5,3,1,4,3,5,2,4,2]
# print("ans :",s.constructDistancedSequence()) # 



