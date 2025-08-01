# 2140. Solving Questions With Brainpower
# https://leetcode.com/problems/solving-questions-with-brainpower/description/

from typing import List
import functools

# my 39ms Beats99.46%
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        mem = [0]*len(questions)
        max_sum = 0
        max_ans = 0
        for i, (po, br) in enumerate(questions):
            if mem[i] > max_sum :
                max_sum = mem[i]
            new_sum = max_sum + po
            # print(max_sum, new_sum)
            fut_i = i+br+1
            if fut_i < len(mem) :
                if new_sum > mem[fut_i] :
                    mem[fut_i] = new_sum
            elif new_sum > max_ans : # 到底了
                max_ans = new_sum 
        return max_ans

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
    
# my v2 55ms Beats98.15%
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



