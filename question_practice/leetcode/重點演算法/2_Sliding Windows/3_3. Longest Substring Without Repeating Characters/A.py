# My Runtime: 64 ms, faster than 89.01% of Python3
class Solution:
    def lengthOfLongestSubstring(self, s):
        l = 0
        seen = set()
        max_len = 0
        for r,r_word in enumerate(s):
            if r_word in seen :
                # print(seen)
                while s[l] != r_word :
                    # print(s[l], l)
                    seen.remove(s[l])
                    l += 1
                l += 1
            else :
                seen.add(r_word)
                max_len = max(r-l+1, max_len)
            
            
        return max_len

s = Solution()
# print(s.lengthOfLongestSubstring("abcabcbb"))
# print(s.lengthOfLongestSubstring("pwwkew"))
