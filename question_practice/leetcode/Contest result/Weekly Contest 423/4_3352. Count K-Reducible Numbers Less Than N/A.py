# 3352. Count K-Reducible Numbers Less Than N
# https://leetcode.com/problems/count-k-reducible-numbers-less-than-n/

from typing import List
from math import inf
from functools import cache

# my inspire by given ans : 4766ms Beats14.81%
    # 但這裡有一個s pecail case是 001 其實是 1 : 這裡只是剛好 ops(1) <= k 而已 !!
@cache
def cal_k(n):
    if n == 1 :
        return 0
    return cal_k(n.bit_count())+1

MOD = 10**9+7
class Solution:
    def countKReducibleNumbers(self, s: str, k: int) -> int:
        len_n = len(s)
        @cache
        def cal_comb(now_pos, rem_cnt1, same_s_cnt):
            if (len_n-now_pos) == rem_cnt1 : # 剩餘的1 數量剛好
                if same_s_cnt : # 因為這個數字不包含
                    return 0
                return 1
            if now_pos == len_n : # 到底了
                return 0
            
            ret_comb = 0
            # take 
            if same_s_cnt : # able to take condition
                if s[now_pos] == "1" :
                    ret_comb = cal_comb(now_pos+1, rem_cnt1-1, True)
                    # 還可以選0 也就是下面的 dont take
                else :
                    # 只能選0
                    return cal_comb(now_pos+1, rem_cnt1, True)
            else : # 前面不一樣
                ret_comb = cal_comb(now_pos+1, rem_cnt1-1, False)

            # dont take
            ret_comb += cal_comb(now_pos+1, rem_cnt1, False)

            if ret_comb >= MOD :
                ret_comb -= MOD
            # if ret_comb >= MOD : 
            #     raise Exception("need MOD")
            return ret_comb
        # given ans template : shorter but slower
        # def cal_comb(now_pos, rem_cnt1, same_s_cnt):
        #     if now_pos == len_n :
        #         return 0 if same_s_cnt or rem_cnt1 else 1
        #     up = int(s[now_pos]) if same_s_cnt else 1
        #     res = 0
        #     for d in range(min(up, rem_cnt1) +1):
        #         res += cal_comb(now_pos+1, rem_cnt1-d, same_s_cnt and d == up)
        #     return res%MOD

        # 先按一次，讓數字範圍不要太大 > 所以結果要找 k-1 以下的
        ans_cnt = 0
        for poss_cnt1 in range(1, len(s)+1) : # 1 開始，因為0最終不會到1
            if cal_k(poss_cnt1) < k : # 因為是 k-1，所以不是 <= 
                ans_cnt += cal_comb(0, poss_cnt1, True)
        cal_comb.cache_clear()
        return ans_cnt % MOD
    
# given ans : 1708ms Beats66.67%
    # 我用 DP 拓展所有可能，然後再判斷這些可能是否符合
    # 因為很多結果是前面就計算過了，所以可行
        # 但前提還是要想到 先按一下
    # 但這裡有一個s pecail case是 001 其實是 1 : 這裡只是剛好 ops(1) <= k 而已 !!
@cache
def ops(ones):
    if ones==1: return 1
    return 1+ops(ones.bit_count())
class Solution:
    def countKReducibleNumbers(self, s: str, k: int) -> int:
        @cache
        def dp(i, ones, less):
            nonlocal k
            if i==len(s):
                if ones!=0 and ops(ones)<=k and less==1:
                    return 1
                return 0
            res = 0
            if less: # 如果前面不相同 : take / don't take
                take1 = dp(i+1, ones+1, less)
                take0 = dp(i+1, ones, less)
                return take1 + take0
            else:
                if s[i]=='0': # 如果前面相同 且此數為 0 : 只能 don't take
                    return dp(i+1, ones, less)
                else: # 如果前面相同 但此數為 1
                    take1 = dp(i+1, ones+1, less) # take
                    take0 = dp(i+1, ones, 1)  # don't take 會變成與前面不符
                    return take1 + take0
        return dp(0, 0, 0) % MOD

s = Solution()
print("ans :",s.countKReducibleNumbers(s = "111", k = 1)) # 3
# print("ans :",s.countKReducibleNumbers(s = "1", k = 3)) # 0

print("ans :",s.countKReducibleNumbers(s = "11", k = 1)) # 2
print("ans :",s.countKReducibleNumbers(s = "1000", k = 2)) # 6



