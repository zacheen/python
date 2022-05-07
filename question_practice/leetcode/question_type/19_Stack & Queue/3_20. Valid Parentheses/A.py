# my Runtime: 45 ms, faster than 45.98% of Python3
# 要快用計數的就好了 但這裡是要練習stack
# class Solution:
#     def isValid(self, s):
#         corr = {'(': ')', '{': '}', '[' : ']'}
#         stack = []
#         for item in s:
#             if stack and item == stack[-1] :
#                 top = stack.pop()
#             else :
#                 ret = corr.get(item,None)
#                 if ret == None :
#                     return False
#                 else :
#                     stack.append(ret)
#         # print(stack)
#         return not stack

# given ans
# 有時候append的條件比較簡單 可以先判斷這個 剩下的再處理
class Solution:
    def isValid(self, s):   
        stack = []
        for c in s:
            if c == '(':
                stack.append(')')
            elif c == '{':
                stack.append('}')
            elif c == '[':
                stack.append(']')
            elif not stack or stack.pop() != c:
                return False

        return not stack

s = Solution()
print(s.isValid("()[]{}"))
print(s.isValid("()[{}]"))
print(s.isValid("(]"))



