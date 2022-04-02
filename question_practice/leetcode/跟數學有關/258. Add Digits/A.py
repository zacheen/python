# My Runtime: 36 ms, faster than 82.83% of Python3
class Solution:
    def addDigits(self, num: int):
        while num >= 10 :
            temp = 0
            while num > 0 :
                temp = temp + num % 10
                num = num //10
            num = temp
        return num

# 另外有一個篇數學的解法 是找除9的餘數

s = Solution()
print(s.addDigits(38))

