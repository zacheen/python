# my Runtime: 426 ms, faster than 5.14% of Python3
# 比較難在找規律上面
# class Solution:
#     def calculate(self, s):
#         s = "("+s.replace(" ","")+")"
        
#         stack = []
#         num = 0
#         for indx, this_c in enumerate(s) :
#             # print(indx, this_c)
#             if this_c.isdecimal() :
#                 num = num*10 + int(this_c)
#                 if not s[indx+1].isdecimal() :
#                     stack.append(num)
#                     num = 0

#                     # 如果可以計算就先計算
#                     if len(stack) >= 3 :
#                         if stack[-2] == "+" :
#                             stack[-3] += stack[-1]
#                             stack = stack[:-2]
#                         elif stack[-2] == "-" :
#                             # print(stack)
#                             stack[-3] -= stack[-1]
#                             stack = stack[:-2]
#             elif this_c == ")":
#                 # print("must be (", stack[-2])
#                 del(stack[-2])

#                 # 如果可以計算就先計算
#                 if len(stack) >= 3 :
#                     if stack[-2] == "+" :
#                         stack[-3] += stack[-1]
#                         stack = stack[:-2]
#                     elif stack[-2] == "-" :
#                         stack[-3] -= stack[-1]
#                         stack = stack[:-2]
            
#             else :
#                 if this_c == "-" and s[indx-1]=="(":
#                     stack.append(0)
#                 stack.append(this_c)

#             # print(stack)
#         return stack[-1]
                

# given ans
# 計算到目前這個位置 是+還是-
class Solution:
    def calculate(self, s):
        ans = 0
        num = 0
        sign = 1
        stack = [sign]  # stack[-1]: current env's sign

        for c in s:
            if c.isdigit():
                num = num * 10 + (ord(c) - ord('0'))
            elif c == '(':
                stack.append(sign)
            elif c == ')':
                stack.pop()
            elif c == '+' or c == '-':
                ans += sign * num
                sign = (1 if c == '+' else -1) * stack[-1]
                num = 0

            # print(c, ans , sign , num)

        return ans + sign * num

s = Solution()
# print(s.calculate("1+1"))
print(s.calculate("-2"))
# print(s.calculate(" 2-1 + 2 "))
# print(s.calculate("(1+(4+5+2)-3)+(6+8)"))
# print(s.calculate("-2+ 1"))
# print(s.calculate("((3)+(1+1+(0))-(-1-(-1-(-1+1))))"))
# print(s.calculate("10-(10)"))

# print(s.calculate("5+3-4-(1+2-7+(10-1+3+5+(3-0+(8-(3+(8-(10-(6-10-8-7+(0+0+7)-10+5-3-2+(9+0+(7+(2-(2-(9)-2+5+4+2+(2+9+1+5+5-8-9-2-9+1+0)-(5-(9)-(0-(7+9)+(10+(6-4+6))+0-2+(10+7+(8+(7-(8-(3)+(2)+(10-6+10-(2)-7-(2)+(3+(8))+(1-3-8)+6-(4+1)+(6))+6-(1)-(10+(4)+(8)+(5+(0))+(3-(6))-(9)-(4)+(2))))))-1)))+(9+6)+(0))))+3-(1))+(7))))))))"))

