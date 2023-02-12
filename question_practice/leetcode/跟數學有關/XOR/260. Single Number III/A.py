# my Beats 81.82%
# class Solution(object):
#     def singleNumber(self, nums):
#         mem_set = set()
#         for n in nums :
#             if n in mem_set :
#                 mem_set.remove(n)
#             else :
#                 mem_set.add(n)
#         return list(mem_set)

# given ans
# 解釋 : https://www.youtube.com/watch?v=LxcX_NVHep4
# 我們先找到 A^B 的結果 (全部的數字 ^ 起來)
# 然後再用 (A^B) & -(A^B) 可以找到 A 跟 B 在某個位置 Bit Number 不同
# 再 for 迴圈一次
    #if num & lowbit:
        # 這個是把跟 A 跟在 其他跟  lowbit 位置同為 Bit Number 的全部數字 ^ 起來
            # -> A ^ [X ^ X ^ Y ^ Y ^ Z ^ Z ...] 後面的數字一定都是成雙的
    # else:
        # 相反     
            # -> B ^ [a ^ a ^ b ^ b ^ c ^ c ...] 後面的數字一定都是成雙的 且 跟上面的數字不會重複

import functools
import operator
class Solution:
    def singleNumber(self, nums):
        xors = functools.reduce(operator.xor, nums)
        lowbit = xors & -xors
        ans = [0, 0]

        # Seperate nums into two groups by the lowbit
        for num in nums:
            if num & lowbit:
                ans[0] ^= num
            else:
                ans[1] ^= num

        return ans

s = Solution()
print(s.singleNumber([1,2,1,3,2,5]))
print(s.singleNumber([-1,0]))
print(s.singleNumber([0,1]))



