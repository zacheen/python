# my 
# class Solution:
#     def maximumCandies(self, candies, k):
#         left, right = 0, max(candies)
#         while left+1 < right:
#             # print(left, right)
#             mid = (left + right)//2
            
#             # 計算可以滿足的人數
#             total = 0
#             for can in candies :
#                 total += can//mid
            
#             if total >= k :
#                 left = mid
#             else:
#                 right = mid

#         # 計算 l,r 哪個是答案
#         print("final :",left, right)
#         total = 0
#         for can in candies :
#             total += can//right
#         if total >= k :
#             return right
#         else :
#             return left

# given ans
# 優化計人數是用減的 這樣到0就可以break
# class Solution(object):
#     def maximumCandies(self, candies, k):
#         m, l = 0, 0
#         for c in candies:
#             m = max(c, m)
#         def c(t, k):
#             for c in candies:
#                 k -= c / t
#                 if k <= 0:
#                     break
#             return k <= 0
#         if c(m, k):
#             return m
#         while m - l > 1:
#             print(m , l)
            
#             if (c((m + l) / 2, k)):
#                 l = (m + l) / 2
#             else:
#                 m = (m + l) / 2
#         # (O)
#         # 他怎麼能確保每次答案都是在l ?
#         # (m + l) / 2 不會產生小數點嗎 ?  有ㄟ...
#             # 因為是用小數
#             # 所以可以想成 m是從最大的數開始 第一個超過可以的解的答案 也就是最大的那一個解
#                 # 所以只要r符合 就會從 if c(m, k): return m 結束
#                 # 所以沒有結束一定是 l
#             # 又因為 強制回傳 int 所以會自動轉型
#         return l

# given ans 判斷又更少...
class Solution:
    def maximumCandies(self, a, k):
        L = 0
        R = max(a)+1  # 是因為加一 所以每次R都不會符合結果
        while L < R - 1:
            M = (L + R) // 2
            s = 0
            for i in a:
                s += i // M
            if s >= k:
                L = M
            else:
                # (O)
                # 進來這裡的時候 每次都是不符合結果的時候 所以R一定不會符合結果
                # 所以 l 一定是最大的答案
                R = M
        return L

s = Solution()
print("ans:",s.maximumCandies([4,7,6],3))
# print(s.maximumCandies([5,5,5],3))
# print(s.maximumCandies([2,5],11))


