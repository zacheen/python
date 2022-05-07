# my Runtime: 105 ms, faster than 65.05% of Python3
class Solution:
    def calculate(self, s):
        s = s.replace(" ","")
        
        stack = []
        sign = 1
        now_num = None
        for indx, c in enumerate(s) :
            if c.isnumeric():
                if now_num == None :
                    now_num = int(c)
                else :
                    now_num = now_num*10 + int(c)

                # 檢查後面還有沒有數字
                if not(indx+1 < len(s) and s[indx+1].isnumeric()) :
                    # 如果沒有數字就加入 stack
                    stack.append(sign*now_num)
                    sign = 1
                    now_num = None

                    # 如果是乘除就先做 
                    if len(stack) >= 3 :
                        if stack[-2]=="*" :
                            stack[-3] *= stack[-1]
                            stack = stack[:-2]
                        elif stack[-2]=="/" :
                            stack[-3] = int(stack[-3]/stack[-1])
                            stack = stack[:-2]
            
            elif c == "+" :
                sign = 1
            elif c == "-" :
                sign = -1
            else :
                stack.append(c)

            # print(stack)

        return sum(stack)

# given ans
# 紀錄前一個狀態(符號)  當新的符號出現後就使用上一個符號進行計算
# 但 2/-2 這種情況是如何解決的?
#    靠腰 給我跳錯 應該是沒有這種 testcase
# class Solution:
#     def calculate(self, s):
#         ans = 0
#         prevNum = 0
#         currNum = 0
#         op = '+'

#         for i, c in enumerate(s):
#             if c.isdigit():
#                 currNum = currNum * 10 + int(c)
#             if not c.isdigit() and c != ' ' or i == len(s) - 1:
#                 if op == '+' or op == '-':
#                     ans += prevNum
#                     prevNum = currNum if op == '+' else -currNum
#                 elif op == '*':
#                     prevNum = prevNum * currNum
#                 elif op == '/':
#                     prevNum = int(prevNum / currNum)
#                 op = c
#                 currNum = 0

#             # print(c, ans, prevNum, currNum)

#         return ans + prevNum

s = Solution()
# print(s.calculate("2+2"))
# print(s.calculate("2-2"))
# print(s.calculate("-2-2"))
# print(s.calculate("2/-2"))
# print(s.calculate("3+5 / 2")) # 5
# print(s.calculate("14-3/2")) # 13
