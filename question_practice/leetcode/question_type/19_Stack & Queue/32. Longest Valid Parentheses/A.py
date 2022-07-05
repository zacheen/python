# my Runtime: 45 ms, faster than 86.72% of Python3 
class Solution:
    def longestValidParentheses(self, s):
        stack = [")",")"] 
        # 先放一個 ")",")" 是為了避免 stack[-1] 跟 stack[-2] outofrange
        
        for c in s :
            if c == "(" :
                stack.append("(")
            else :
                if stack[-1] == "(" :
                    del(stack[-1])
                    stack.append(2)
                elif stack[-2] == "(" :
                    del(stack[-2])
                    stack.append(2)
                else :
                    stack.append(")")

                # 合併尾端數字
                if type(stack[-1]) == int :
                    while type(stack[-2]) == int :
                        stack[-1] = stack[-2]+stack.pop()
            # print(stack)
        
        max_ans = 0
        for i in stack :
            if type(i)==int :
                max_ans = max(max_ans, i)
        return max_ans 
        # 如果 stack 裡面沒有 "(" ")" 的話 
        # 直接 max(stack) 比較快
        

# given ans Runtime: 46 ms, faster than 85.02% of Python3
# class Solution:
#     def longestValidParentheses(self, s):
#         s2 = ')' + s
#         # dp[i] := length of longest valid parentheses substring of s2[1..i]
#         dp = [0] * len(s2)

#         for i in range(1, len(s2)):
#             # dp[i - 1] 是 前一個")"到對應的"(" 同個level(被包在同一個括號裡面)裡面有幾個合理的括號組
#             # [i - dp[i - 1] - 1] 是此位置如果要配對成合理的括號組 就一定要是 '('
#             if s2[i] == ')' and s2[i - dp[i - 1] - 1] == '(':
#                 # dp[i - dp[i - 1] - 2] 是前一組() 最長的可能性
#                 dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
#             # print(dp)
#         return max(dp)

s = Solution()
# print(s.longestValidParentheses("(()"))
# print(s.longestValidParentheses(")()()("))
# print(s.longestValidParentheses("()(()"))  # commit fail
print(s.longestValidParentheses("(()()(()))"))
# print(s.longestValidParentheses("())(())"))  # commit fail
# print(s.longestValidParentheses())



