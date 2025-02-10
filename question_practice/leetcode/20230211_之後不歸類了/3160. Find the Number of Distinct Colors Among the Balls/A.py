# 3160. Find the Number of Distinct Colors Among the Balls
# https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/description

from typing import List

from collections import defaultdict, Counter

# my 84ms Beats37.70%
class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        mem = {}
        cou = defaultdict(int)
        ans = 0
        ans_l = []
        for indx, color in queries :
            if indx in mem :
                pre_c = mem[indx]
                cou[pre_c] -= 1
                if cou[pre_c] == 0:
                    ans -= 1
            if cou[color] == 0 :
                ans += 1
            cou[color] += 1
            mem[indx] = color
            ans_l.append(ans)
        return ans_l

# given ans
# same concept, but optimized : using colorCount to trace ans count
class Solution:
    def queryResults(self, limit: int, queries: list[list[int]]) -> list[int]:
        ans = []
        ballToColor = {}
        colorCount = Counter()

        for ball, color in queries:
            if ball in ballToColor:
                prevColor = ballToColor[ball]
                colorCount[prevColor] -= 1
                if colorCount[prevColor] == 0:
                    del colorCount[prevColor]
            ballToColor[ball] = color
            colorCount[color] += 1
            ans.append(len(colorCount))
        return ans

s = Solution()
print("ans :",s.queryResults(limit = 4, queries = [[1,4],[2,5],[1,3],[3,4]])) # [1,2,2,3]



