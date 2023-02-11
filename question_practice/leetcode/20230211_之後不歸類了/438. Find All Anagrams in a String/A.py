# my 
# 條件 : count 的結果相同 (較慢)
# from collections import Counter
# class Solution(object):
#     def findAnagrams(self, s, p):
#         if len(s)<len(p) :
#             return []

#         c = Counter(p)
#         ans = []
#         sliding_window = Counter(s[:len(p)])

#         sliding_window_len = len(p)
#         for i in range(len(s)-len(p)) :
#             if(c == sliding_window):
#                 ans.append(i)
#             sliding_window[s[i]] -= 1
#             if (sliding_window[s[i]] == 0):
#                 del(sliding_window[s[i]])
#             sliding_window[s[i+sliding_window_len]] += 1
#             # print(sliding_window)
#         if(c == sliding_window):
#             ans.append(len(s)-len(p))
#         return ans

# given ans
# 條件 : required 數量歸零 (判斷 == 0 較快)
class Solution(object):
    def findAnagrams(self, s, p):
        ans = []
        count = Counter(p)
        required = len(p)

        for r, c in enumerate(s):
            count[c] -= 1
            if count[c] >= 0:
                required -= 1
            if r >= len(p):
                count[s[r - len(p)]] += 1
                if count[s[r - len(p)]] > 0:
                    required += 1
            if required == 0:
                ans.append(r - len(p) + 1)

        return ans

s = Solution()
print(s.findAnagrams(s = "cbaebabacd", p = "abc"))
print(s.findAnagrams(s = "abab", p = "ab"))
# print(s.findAnagrams())



