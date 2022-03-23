# 從前面開始加 stack 
# 如果遇到相同的字母 先判斷是否能整除 再進 def 判斷
# My Runtime: 96 ms, faster than 53.21% of Python3 
class Solution:
    def repeatedSubstringPattern(self, s):
        def check_repeat(rep):
            # ------------------------------
            # 方法1
            # idx = len(rep)
            # while idx < len(s) :
            #     if s[idx:idx+len(rep)] != rep :
            #         return False
            #     idx += len(rep)
            # return True
            # ------------------------------
            # 方法2
            res = s.split(rep)
            if "".join(res) == "":
                return True
            else:
                return False
            # ------------------------------
            

        for i in range(1,len(s)//2+1) :
            repeat = s[:i]
            if s[i] == repeat[0] :
                if len(s) % len(repeat) == 0 :
                    if check_repeat(repeat) == True :
                        return True
        return False

# given ans 
# 邏輯是 再加上一次自己一定也會重複
# 所以除了原本的字串([1:-1]) 如果能夠找到原本的字串 一定是重複的字串                 
# class Solution:
#     def repeatedSubstringPattern(self, s):  
#         return s in (s + s)[1:-1]

s = Solution()
# print(s.repeatedSubstringPattern("ababab"))
print(s.repeatedSubstringPattern("aaaaaa"))
# print(s.repeatedSubstringPattern("abcdef"*30))