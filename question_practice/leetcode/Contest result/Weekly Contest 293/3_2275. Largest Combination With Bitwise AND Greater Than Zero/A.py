# my
# 轉成 bin
# 計算每個位置 的 1 共有幾個
# 找出最大的 
class Solution(object):
    def largestCombination(self, candidates):
        count = [0]*25 # 最前面是最後一位
        for n in candidates :
            s = bin(n)[2:]
            for indx, c in enumerate(reversed(s)) :
                if c == "1" :
                    count[indx] += 1
        return max(count)
            

# given ans
# class Solution(object):
#     def largestCombination(self, candidates):
#         a, r = [0] * 30, 0
#         for n in candidates:
#             v, i = 1, 0
#             for i in range(1, 30):
#                 a[i],r = \
#                     a[i] + (1 if v & n else 0), \
#                     max(r, a[i] + (1 if v & n else 0)) if v & n else r
#                 v = v << 1
#                 print(a)
#                 if v > n :
#                     break
#         return r

s = Solution()
print(s.largestCombination([16,17,71,62,12,24,14]))



