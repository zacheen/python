# Runtime: 114 ms, faster than 86.60% of Python3
class Solution:
    def validPalindrome(self, s):
        l, r = 0, len(s)-1
        
        have_diff = False
        while l < r :
            # print(l , r)
            if s[l] != s[r] :
                # 不能用 else if 
                # 要不然當 s[l+1] == s[r] 和 s[l] == s[r-1] 兩邊同時符合的時候 不知道要走哪一條
                if s[l+1] == s[r] :
                    remain_str = s[l+1:r+1]
                    # print("1",remain_str, remain_str[::-1])
                    if remain_str == remain_str[::-1] :
                        return True
                if s[l] == s[r-1] :
                    remain_str = s[l:r]
                    # print("2",remain_str, "".join(list(reversed(remain_str))))
                    if remain_str == remain_str[::-1] :
                        return True
                return False
            l += 1
            r -= 1
        return True

# given ans
# 比較的時候真的算出中間點  再反轉比較
# s[i] != s[~i] 或 s[i] != s[-i] 這樣就不用紀錄 r  
# class Solution:
#     def validPalindrome(self, s: str) -> bool:
#         def validPalindrome(l: int, r: int) -> bool:
#             return all(s[i] == s[r - i + l] for i in range(l, l + (r - l) // 2 + 1))

#         n = len(s)

#         for i in range(n // 2):
#             if s[i] != s[~i]:
#                 return validPalindrome(i + 1, n - 1 - i) or validPalindrome(i, n - 2 - i)

#         return True

s = Solution()
# aguokepatgbnvfqmgml c upuufxoohdfpgjdmysgvhmvffcnqxj
# jxqncffvmhvgsymdjgpfdhooxfuupucu  lmgmqfvnbgtapekouga
# print(s.validPalindrome("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"))
print(s.validPalindrome("lcupuupucul"))

# 1
# upuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupucu 
# ucupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupu

# 2
# cupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuc
# cupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuc
