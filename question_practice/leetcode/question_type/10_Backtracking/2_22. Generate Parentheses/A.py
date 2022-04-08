# given ans
# 推理出規則 : 到任何一點 左括號的數量不會小於右括號的數量
class Solution:
    def generateParenthesis(self, n):
        ans = []

        def dfs(l: int, r: int, s: str):
            if l == 0 and r == 0:
                ans.append(s)
            if l > 0:
                dfs(l - 1, r, s + '(')
            if l < r:
                dfs(l, r - 1, s + ')')

        dfs(n, n, '')
        return ans



s = Solution()
print(s.generateParenthesis(3))



