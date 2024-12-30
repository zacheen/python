# 3395. Subsequences with a Unique Middle Mode I
# https://leetcode.com/problems/subsequences-with-a-unique-middle-mode-i/description/

from typing import List
import functools

# given ans 2204ms Beats81.07%
MOD = 10**9+7
comb2 = lambda x: x * (x-1) // 2 # C x 取 2
class Solution:
    def subsequencesWithMiddleMode(self, nums: List[int]) -> int:
        # discrete to dense
        mp = {x: i for i, x in enumerate(set(nums))}
        nums = [mp[x] for x in nums]
        n = len(nums)

        # mem the count at indx i
        pres = [[0] * len(mp)]
        for x in nums:
            pres.append(pres[-1].copy())
            pres[-1][x] += 1
        
        ans = 0
        for i in range(2, n-2):
            oth_side_i = (n-1-i)
            c = nums[i]
            l = pres[i][c] # 左邊的 c 有幾個
            r = pres[n][c] - pres[i+1][c] # 右邊的 c 有幾個
            # 為什麼不用 -1 : 因為是 i+1，已經排除這一格的 c 了
            res = comb2(i) * comb2(oth_side_i) # 全部的組合的個數
            # 為什麼不一開始就直接全部加起來 " 因為這個組合是假設 c 在中間
            res -= comb2(i-l) * comb2(oth_side_i-r) # 減去全部 c 不為中位數的情況 (包含 11111, 311 ...) (當 l 與 r 同時為 0 時 會等餘上面的公式)
            # 排除其他數字比較大的組合 (y 為其他數字)
            # 排除 221 且 c 在中間的情況
            for y in range(len(mp)): # for 全部的數字
                if y == c: continue
                ly = pres[i][y] # 左邊的y
                ry = pres[n][y] - pres[i+1][y] # 右邊的y
                lz = i - l - ly # 左邊的其他數字(排除 y跟c )
                rz = oth_side_i - r - ry # 右邊的其他數字(排除 y跟c )
                res -= l*ly*ry*rz # 左邊選一個y 一個c, 右邊選一個y 一個其他
                res -= lz*ly*ry*r # 左邊選一個y 一個其他, 右邊選一個y 一個c
                res -= l*(i-l)*comb2(ry) # 右邊選兩個y, 左邊兩個其他
                res -= r*(oth_side_i-r)*comb2(ly) # 左邊選兩個y, 右邊兩個其他
            ans = (ans + res) % MOD
        return ans

# # my fail
# # missing "A sequence of numbers seq of size 5 contains a unique middle mode if the middle element (seq[2]) is a unique mode."
# from collections import Counter
# MOD = 10**9 + 7
# class Solution:
#     def subsequencesWithMiddleMode(self, nums: List[int]) -> int:
#         @functools.lru_cache(None)
#         def C_t_get_n(t, n):
#             if n == 0 or t<n : return 0
#             if t == n : return 1
#             if t//2 < n : return C_t_get_n(t, t-n)
#             if n > 1 :
#                 return C_t_get_n(t, n-1) * (t-n+1) // (n)
#             if n != 1 :
#                 raise Exception
#             return t
        
#         cout = Counter(nums)
#         n_list = [k for k in cout]
#         total_comb = C_t_get_n(len(nums), 5) % MOD
#         # 11111 5 diff
#         total_comb -= C_t_get_n(len(cout), 5) % MOD
#         # 221 
#         for indx, n1 in enumerate(n_list) :
#             if cout[n1] >= 2 :
#                 for n2 in n_list[indx+1:] :
#                     if cout[n2] >= 2 :
#                         n1_c = cout[n1]
#                         n2_c = cout[n2]
#                         l = [C_t_get_n(n1_c, 2), C_t_get_n(n2_c, 2), (len(nums) - n1_c - n2_c)]
#                         total_comb = (total_comb - C_t_get_n(n1_c, 2) * C_t_get_n(n2_c, 2) * (len(nums) - n1_c - n2_c)) % MOD
#         return total_comb

s = Solution()
# print("ans :",s.subsequencesWithMiddleMode(nums = [1,1,1,1,1,1])) # 6
# print("ans :",s.subsequencesWithMiddleMode(nums = [1,2,2,3,3,4])) # 4
# print("ans :",s.subsequencesWithMiddleMode(nums = [2,3,3,4,4,5])) # 4
# print("ans :",s.subsequencesWithMiddleMode(nums = [0,1,2,3,4,5,6,7,8])) # 0
# print("ans :",s.subsequencesWithMiddleMode(nums = [0,1,-1,1,1])) # 0
# print("ans :",s.subsequencesWithMiddleMode(nums = [0,1,-1,1,1])) # 0
# print("ans :",s.subsequencesWithMiddleMode(nums = [0,1,-1,-1,1])) # 0
print("ans :",s.subsequencesWithMiddleMode(nums = [0,1,-1,0,1])) # 0



