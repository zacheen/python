# 3031. Minimum Time to Revert Word to Initial State II
# https://leetcode.com/problems/minimum-time-to-revert-word-to-initial-state-ii/description/

# 解法同
# 3029. Minimum Time to Revert Word to Initial State I
# https://leetcode.com/problems/minimum-time-to-revert-word-to-initial-state-i/description/

from typing import List
import functools

# my 0ms Beats100.00%
class Solution:
    def minimumTimeToInitialState(self, s: str, k: int) -> int:
        len_s = len(s)
        z = [0]*len_s
        z_box_l = z_box_r = 0
        for i in range(k, len_s, k):
            same_len = 0
            if i <= z_box_r :
                same_len = min(z_box_r-i+1, z[i-z_box_l])
                    # z_box_r-i+1  : 如果 i~z_box_r 全部都一樣，長度會是多少
                    # z[i-z_box_l] :  為了排除情況 "aabab"
                # print(same_len) # 應該要大於1 才會 fast forward
            while i + same_len < len_s and s[same_len] == s[i+same_len]:
                # 這裡順序不能錯
                z_box_l = i
                z_box_r = i + same_len
                same_len += 1
            z[i] = same_len

            if z[i] >= len_s - i:
                return i // k
        return ((len_s - 1) // k) + 1

s = Solution()
print("ans :",s.minimumTimeToInitialState(word = "abacaba", k = 3)) # 2
print("ans :",s.minimumTimeToInitialState(word = "abacaba", k = 4)) # 1
print("ans :",s.minimumTimeToInitialState(word = "abcbabcd", k = 2)) # 4



