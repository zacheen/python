# My Runtime: 39 ms, faster than 79.86% of Python3
class Solution:
    def getLucky(self, s, k):
        sum = ""
        for each_word in s :
            sum = sum + str(ord(each_word)-96)
            
        print(sum)
        sum = int(sum)

        for i in range(k):
            temp = 0
            while sum > 0 :
                temp = temp + sum % 10
                sum = sum // 10
            sum = temp

        return sum

s = Solution()
# print(s.getLucky("iiii",1))
# print(s.getLucky("zbax",2))
print(s.getLucky("leetcode",2))
