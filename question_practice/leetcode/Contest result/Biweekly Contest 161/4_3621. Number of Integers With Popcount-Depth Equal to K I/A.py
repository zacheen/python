# 3621. Number of Integers With Popcount-Depth Equal to K I
# https://leetcode.com/problems/number-of-integers-with-popcount-depth-equal-to-k-i/description/
    # 跟這題很像，只是把 <= k 變成 == k
    # 3352. Count K-Reducible Numbers Less Than N
    # https://leetcode.com/problems/count-k-reducible-numbers-less-than-n/

from typing import List
from math import inf
from functools import cache

# my 51msBeats68.36%
@cache
def ops(ones):
    if ones == 1 : return 1
    return ops(ones.bit_count())+1
class Solution:
    def popcountDepth(self, n: int, k: int) -> int:
        if k == 0 :
            return 1 # 就只有剛好是 1 這個 case
        
        s = f'{n:b}'
        @cache
        def dp(i, ones, less):
            nonlocal k
            if i==len(s):
                if ones!=0 and ops(ones) == k:
                    return 1
                return 0

            if less: # 如果前面不相同 : take / don't take
                take1 = dp(i+1, ones+1, less)
                take0 = dp(i+1, ones, less)
                return take1 + take0
            else:
                if s[i]=='0': # 如果前面相同 且此數為 0 : 只能 don't take
                    take0 = dp(i+1, ones, less)
                    return take0
                else: # 如果前面相同 但此數為 1
                    take1 = dp(i+1, ones+1, less) # take
                    take0 = dp(i+1, ones, 1)  # don't take 會變成與前面不符
                    return take1 + take0
        
        all_comb = dp(0, 0, 0)
        if k == 1:
            all_comb -= 1 # 要扣除 case 0...01 的這個case 因為 ones是1 但其實 k是0
        return all_comb


s = Solution()
print("ans :",s.popcountDepth(n = 4, k = 1)) # 2
print("ans :",s.popcountDepth(n = 7, k = 2)) # 3

# edge test case
print("ans :",s.popcountDepth(n = 1, k = 0)) # 1

