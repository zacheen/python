# 5. Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/description/

# my Runtime: 119 ms, faster than 98.88% of Python3
# 比較次數 O(2n) = 每個位置 + P有可能的長度
# 但我的 is_p 每次是比較 兩個s
# class Solution:
#     def longestPalindrome(self, s):
#         if s == "" :
#             return 
        
#         def is_p(s) :
#             # print(s , s[::-1], s == s[::-1])
#             return s == s[::-1]
        
#         now_max_str = s[0]
        
#         # even
#         now_min_len = 1 # 左右的長度
        
#         # for l in range(len(s)) : # mid
#         #     r = l + now_min_len + 1
#         #     l = l - now_min_len + 1
#         for l in range(1,len(s)+1) : # mid
#             r = l + now_min_len
#             l = l - now_min_len
#             while l >= 0 and r <= len(s) :
#                 if is_p(s[l:r]) :
#                     now_min_len += 1
#                     now_max_str = s[l:r]
#                     l -= 1
#                     r += 1
#                 else :
#                     break
                    
#         # odd
#         now_min_len -= 1 # 左右的長度(不包括中間)
#         for l in range(len(s)) : # mid
#             r = l + now_min_len + 1
#             l = l - now_min_len
#             # print(l,r)
#             while l >= 0 and r <= len(s) :
#                 if is_p(s[l:r]) :
#                     now_min_len += 1
#                     now_max_str = s[l:r]
#                     l -= 1
#                     r += 1
#                 else :
#                     break
                    
#         return now_max_str

# 加入 given ans 的概念再優化
# Runtime: 20ms Beats99.73%
class Solution:
    def longestPalindrome(self, s):
        if s == "" :
            return 
        
        def is_p(s) :
            # print(s , s[::-1], s == s[::-1])
            return s == s[::-1]
        
        now_max_str_l = 0
        now_max_str_r = 1
        
        # even
        now_min_len = 1 # 左右的長度
        for mid in range(1,len(s)+1) :
            r = mid + now_min_len
            l = mid - now_min_len
            if l >= 0 and r <= len(s) and is_p(s[l:r]) :
                now_min_len += 1
                now_max_str_l = l
                now_max_str_r = r
                l -= 1
                # 不用 r += 1 因為 while 是比位置
                while l >= 0 and r < len(s) and s[l] == s[r] :
                    now_max_str_l = l
                    l -= 1
                    r += 1
                    now_max_str_r = r
                    now_min_len += 1

                    
        # odd
        now_min_len -= 1 # 左右的長度(不包括中間)
        for mid in range(len(s)) : # mid
            r = mid + now_min_len + 1
            l = mid - now_min_len
            if l >= 0 and r <= len(s) and is_p(s[l:r]) :
                now_min_len += 1
                now_max_str_l = l
                now_max_str_r = r
                l -= 1
                # r += 1 因為 while 是比位置
                while l >= 0 and r < len(s) and s[l] == s[r] :
                    now_max_str_l = l
                    l -= 1
                    r += 1
                    now_max_str_r = r
                    now_min_len += 1
                    
        return s[now_max_str_l : now_max_str_r]
                    
# given ans
# 比較次數 O(n^2)
# 但每次比較只需要比較一個字母

# 算是用 dp 
# maxExtends 紀錄 目前這個範圍 
# class Solution:
#     def longestPalindrome(self, s):
#         # @ and $ signs are sentinels appended to each end to avoid bounds checking
#         t = '#'.join('@' + s + '$')
#         n = len(t)
#         # t[i - maxExtends[i]..i) ==
#         # t[i + 1..i + maxExtends[i]]
#         maxExtends = [0] * n
#         center = 0

#         for i in range(1, n - 1):
#             rightBoundary = center + maxExtends[center]
#             mirrorIndex = center - (i - center)
#             maxExtends[i] = rightBoundary > i and \
#                 min(rightBoundary - i, maxExtends[mirrorIndex])

#             # Attempt to expand palindrome centered at i
#             while t[i + 1 + maxExtends[i]] == t[i - 1 - maxExtends[i]]:
#                 maxExtends[i] += 1

#             # If palindrome centered at i expand past rightBoundary,
#             # adjust center based on expanded palindrome.
#             if i + maxExtends[i] > rightBoundary:
#                 center = i

#             print(maxExtends)

#         # Find the maxExtend and bestCenter
#         maxExtend, bestCenter = max((extend, i) for i, extend in enumerate(maxExtends))
#         return s[(bestCenter - maxExtend) // 2 : (bestCenter + maxExtend) // 2]

s = Solution()
print(s.longestPalindrome("cbbbbd"))
print(s.longestPalindrome("cbbbbbd"))
print(s.longestPalindrome("aba"))
print(s.longestPalindrome("abcba"))



