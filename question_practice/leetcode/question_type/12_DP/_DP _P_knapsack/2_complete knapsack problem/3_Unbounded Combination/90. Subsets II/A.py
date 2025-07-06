# 90. Subsets II
# https://leetcode.com/problems/subsets-ii/description/

from typing import List
from math import inf

from collections import Counter
# my 0ms Beats100.00%
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        cou = Counter(nums)
        ans = [[]]
        for c,n in cou.items():
            new_item = []
            for i in range(1, n+1) :
                new_item += [a[:]+[c]*i for a in ans]
            ans += new_item
        return ans

# my DFS : 2ms Beats30.14%
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        path = []
        def dfs(i, same_cou) : # return all possible comb
            nonlocal path
            if i == len(nums) :
                ans.append(path.copy())
                return
            this_n = nums[i]
            # 要加入此項
            if path and this_n == path[-1] :
                same_cou += 1
            front = i-same_cou
            # if 跟前面不一樣 or 跟最前面不一樣 
            if (i == 0 or this_n != nums[i-1]) or front == -1 or this_n != nums[front]:
                path.append(this_n)
                dfs(i+1, same_cou)
                path.pop()
            # 不選此項
            dfs(i+1, 1)
        dfs(0,1)
        return ans

# given ans


s = Solution()
# print("ans :",s.subsetsWithDup([1,2,2])) # [[],[1],[1,2],[1,2,2],[2],[2,2]]
print("ans :",s.subsetsWithDup([1,2,2,2]))
# print("ans :",s.subsetsWithDup([0])) # 
print("ans :",s.subsetsWithDup([1,1])) # 



