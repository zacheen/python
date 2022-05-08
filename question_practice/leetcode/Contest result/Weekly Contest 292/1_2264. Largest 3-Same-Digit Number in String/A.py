# 一次 送出失敗
    # 一開始以為是回傳最前面符合的字串
    # 沒看到是要回傳最大的

# my v2  32 ms
class Solution(object):
    def largestGoodInteger(self, num):
        ans = ["999","888","777","666","555","444","333","222","111","000"]
        for a in ans :
            if a in num :
                return a
        return ""

# my v1 44 ms
# class Solution(object):
#     def largestGoodInteger(self, num):
#         max_n = -1
#         n = num[0]
#         count = 0
#         for c in num :
#             if c == n :
#                 count += 1
#                 if count == 3 :
#                     max_n = max(n, max_n)
#             else :
#                 n = c
#                 count = 1
#         if max_n == -1 :
#             return ""
#         else :
#             return n*3

# given ans

s = Solution()
# print(s.largestGoodInteger("6777133339"))
print(s.largestGoodInteger("67771333398887"))



