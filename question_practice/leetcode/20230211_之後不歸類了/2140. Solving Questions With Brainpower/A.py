# 2140. Solving Questions With Brainpower
# https://leetcode.com/problems/solving-questions-with-brainpower/description/

from typing import List
import functools

# my v1 Beats 31.69%
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        @functools.lru_cache(None)
        def dfs(i) :
            if i >= len(questions) :
                return 0
            pick = dfs(i + questions[i][1] + 1) + questions[i][0]
            dont_pick = dfs(i+1)
            # if (pick > dont_pick) :
            #     print(i)
            return max(pick, dont_pick)

        return dfs(0)
    
# my v2 Beats 91.36%
# 但是 我沒有辦法直接想出 for 的寫法 
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        mem = [0]*len(questions)
        mem[-1] = questions[-1][0]
        for i in range(len(questions)-2, -1, -1):
            pick_skip = i + questions[i][1] + 1
            pick_skip_point = questions[i][0]
            if pick_skip < len(questions) :
                pick_skip_point += mem[pick_skip]
            mem[i] = max(mem[i+1], pick_skip_point)
        # print(mem)
        return max(mem)

s = Solution()
# print(s.mostPoints(questions = [[3,2],[4,3],[4,4],[2,5]]))
# print(s.mostPoints(questions = [[1,1],[2,2],[3,3],[4,4],[5,5]]))
print(s.mostPoints([[21,5],[92,3],[74,2],[39,4],[58,2],[5,5],[49,4],[65,3]]))



