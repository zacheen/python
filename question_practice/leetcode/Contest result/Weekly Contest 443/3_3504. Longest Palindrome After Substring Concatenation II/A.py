# 3504. Longest Palindrome After Substring Concatenation II
# https://leetcode.com/problems/longest-palindrome-after-substring-concatenation-ii/description/

from typing import List
from math import inf

# my inspire by given ans : 1901ms Beats78.63%
class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        def sep_longest(long, rev_short):
            # from s : "xyz"+"Palindrome" + from t : "zyx" (reverse of "xyz")  
            # 1. 先計算"xyz"部分 可以在 rev_short 中找到最長的長度
                # 結尾相同的位置放在同一個 list 中，方便之後與"Palindrome"連接
            # 多開一個空間，就不用處理-1的問題
                # front[i+1][j+1] 存此結尾 i,j 最長的"xyz"長度
            front = [[0]*(len(rev_short)+1) for _ in range(len(long)+1)]
            for il, cl in enumerate(long):
                for ir, cr in enumerate(rev_short):
                    if cl == cr: # 若位置相同
                        front[il+1][ir+1] = front[il][ir] + 2
            front_max = [max(each_len) for each_len in front]

            # 2. 找出各個 Palindrome 的位置 + 以i結尾最長的 Palindrome 長度
            max_ans = max(front_max) # 如果沒有 "Palindrome"，最長的結果就是 "xyz"部分
            len_l = len(long)
            def mid_find_pal(l,r):
                nonlocal max_ans
                while l >= 0 and r < len_l and long[l] == long[r]:
                    # l 開頭，所以要找 l-1 位置結尾，front indx 要加1 所以剛好是 l
                    max_ans = max(max_ans, r-l+1 + front_max[l])
                    l -= 1
                    r += 1
            for mid in range(len(long)) :
                # odd
                mid_find_pal(mid,mid)
                # even
                mid_find_pal(mid,mid+1)
            return max_ans
        return max(sep_longest(s,t[::-1]), sep_longest(t[::-1],s))

# given ans : 1447ms Beats82.05%
class Solution:
    def calc(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        f = [[0] * (m + 1) for _ in range(n + 1)]
        for i, x in enumerate(s):
            for j, y in enumerate(t):
                if x == y:
                    f[i + 1][j + 1] = f[i][j] + 1

        mx = list(map(max, f))
        ans = max(mx) * 2 # |x| = |y| 的情況

        # 計算 |x| > |y| 的情況, 中心擴展法
        for i in range(2 * n - 1):
            l, r = i // 2, (i + 1) // 2
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1

            if l + 1 <= r - 1: # s[l+1] 到 s[r-1] 是非空回文串
                ans = max(ans, r - l - 1 + mx[l + 1] * 2)
        return ans

    def longestPalindrome(self, s: str, t: str) -> int:
        return max(self.calc(s, t), self.calc(t[::-1], s[::-1]))

s = Solution()
print("ans :",s.longestPalindrome(s = "a", t = "a")) # 2, aa
print("ans :",s.longestPalindrome(s = "abc", t = "def")) # 1
print("ans :",s.longestPalindrome(s = "b", t = "aaaa")) # 4, aaaa
print("ans :",s.longestPalindrome(s = "abcde", t = "ecdba")) # 5, abcba
print("ans :",s.longestPalindrome("abcde","edcba")) # 10, abcdeedcba
print("ans :",s.longestPalindrome("abcde","dcba")) # 9, abcdedcba
print("ans :",s.longestPalindrome("i","ih")) # 2, ii



