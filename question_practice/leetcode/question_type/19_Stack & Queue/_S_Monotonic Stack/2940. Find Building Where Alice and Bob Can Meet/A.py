# 2940. Find Building Where Alice and Bob Can Meet
# https://leetcode.com/problems/find-building-where-alice-and-bob-can-meet/description

from typing import List
import functools

# Monotonic Stack version 487ms Beats66.67%
class Solution:
    # Similar to 2736. Maximum Sum Queries
    def leftmostBuildingQueries(self, heights, queries):
        ans = [-1] * len(queries)
        # Store indices (heightsIndex) of heights with heights[heightsIndex] in descending order.
        stack = []

        # Iterate through queries and heights simultaneously.
        heightsIndex = len(heights) - 1
        queries = [(i, min(a, b), max(a, b)) for i, (a, b) in enumerate(queries)]
        queries.sort(reverse=True, key=lambda x: x[2])
        for queryIndex, a, b in queries :
            if a == b or heights[a] < heights[b]:
                # 1. Alice and Bob are already in the same index (a == b) or
                # 2. Alice can jump from a -> b (heights[a] < heights[b]).
                ans[queryIndex] = b
            else:
                # Now, a < b and heights[a] >= heights[b].
                # Gradually add heights with an index > b to the monotonic stack.
                while heightsIndex > b:
                    # Monotonic Stack : 存比現在大的數字 且 是遞增的 
                    while stack and heights[stack[-1]] <= heights[heightsIndex]:
                        stack.pop()
                    stack.append(heightsIndex)
                    heightsIndex -= 1
                # Binary search to find the smallest index j such that j > b and
                # heights[j] > heights[a], thereby ensuring heights[j] > heights[b].
                j = self._lastGreater(stack, a, heights)
                if j != -1:
                    ans[queryIndex] = stack[j]
        return ans

    def _lastGreater(self, stack: list[int], target: int, heights: list[int]):
        """
        Returns the last index i in A s.t. heights[A.get(i)] is > heights[target].
        """
        l = -1
        r = len(stack) - 1
        while l < r:
            m = (l + r + 1) // 2
            if heights[stack[m]] > heights[target]:
                l = m
            else:
                r = m - 1
        return l


s = Solution()
print("ans :",s.leftmostBuildingQueries(heights = [6,4,8,5,2,7], queries = [[0,1],[0,3],[2,4],[3,4],[2,2]])) # [2,5,-1,5,2] 
print("ans :",s.leftmostBuildingQueries(heights = [5,3,8,2,6,1,4,6], queries = [[0,7],[3,5],[5,2],[3,0],[1,6]])) # [7,6,-1,4,6]
# print("ans :",s.leftmostBuildingQueries(heights = [3,4,1,2], queries = [[0,0],[0,1],[0,2],[0,3],[1,0],[1,1],[1,2],[1,3],[2,0],[2,1],[2,2],[2,3],[3,0],[3,1],[3,2],[3,3]])) 
# print("ans :",s.leftmostBuildingQueries(heights = [3,4,1,2], queries = [[0,2]])) 



