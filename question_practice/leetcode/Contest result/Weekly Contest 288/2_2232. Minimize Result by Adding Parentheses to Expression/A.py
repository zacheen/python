import math
# my 
class Solution:
    def minimizeResult(self, expression):
        spli = expression.split("+")
        num1 = spli[0]
        num2 = spli[1]
        # print(num1, num2)
        
        def depart(num_s, place):
            if place == 0 :
                return 0, int(num_s)
            if place == len(num_s) :
                return int(num_s), 0
            return int(num_s[:place]), int(num_s[place:])
        
        min_ans = math.inf
        min_s = ""
        for i in range(len(num1)) :
            f1,b1 = depart(num1, i)
            if f1 == 0 :
                chf1 = 1
            else :
                chf1 = f1
            for j in range(1, len(num2)+1) :
                f2,b2 = depart(num2, j)
                if b2 == 0:
                    chb2 = 1
                else :
                    chb2 = b2
                
                cal = chf1 * (b1+f2) * chb2
                if min_ans > cal :
                    min_ans = cal
                    min_s = ""
                    if f1 != 0 :
                        min_s = min_s + str(f1)
                    
                    min_s = min_s + "(" + str(b1) + "+" + str(f2)+ ")"
                    if b2 != 0 :
                        min_s = min_s + str(b2)
                    
        return min_s

# given ans
# 概念差不多
# 不過沒有宣告那麼多變數
# 用位置去紀錄 要用的時候再組
# 不需要先轉 int 
# 保持 str 就好
# 最後組成字串的時候 因為是紀錄位置
# 所以只要插入括號的位置就好

s = Solution()
print(s.minimizeResult("247+38"))
print(s.minimizeResult("12+34"))
print(s.minimizeResult("999+999"))

