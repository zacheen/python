# my Beats 86.28%
class Solution:
    def partitionString(self, s: str):
        ans = 1
        seen = set()
        for c in s :
            if c in seen :
                ans += 1
                seen = set()
            seen.add(c)
        return ans

# given ans
# 因為英文字母最多就 26 個字母
# 所以其實可以用其他方法去紀錄有沒有看過
    # seen = [False]*26

# 這裡是用 binary 去紀錄 (每個位子的 1,0 代表 有沒有看過)
    # 但是比較慢
# Beats 26.52%
# class Solution:
#     def partitionString(self, s: str):
#         ans = 1
#         usedMask = 0
#         for c in s:
#             i = ord(c) - ord('a')
#             if usedMask >> i & 1:
#                 usedMask = 1 << i
#                 ans += 1
#             else:
#                 usedMask |= 1 << i
#         return ans

s = Solution()
print(s.partitionString("abacaba"))
print(s.partitionString("sssss"))



