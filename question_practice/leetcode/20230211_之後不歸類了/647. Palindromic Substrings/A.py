# my Runtime: 133 ms, faster than 76.95% of Python3 
# class Solution:
#     def countSubstrings(self, s: str):
#         ans_count = 0
#         for i in range(len(s)) :
#             l,r = i,i
#             while l >= 0 and r < len(s) :
#                 if s[l] == s[r] :
#                     ans_count += 1 
#                 else :
#                     break
#                 l -= 1
#                 r += 1
        
#         for i in range(len(s)-1) :
#             l,r = i,i+1
#             while l >= 0 and r < len(s) :
#                 if s[l] == s[r] :
#                     ans_count += 1 
#                 else :
#                     break
#                 l -= 1
#                 r += 1
#         return ans_count

# 我想到的合併方法是 直接合併
# 但 given ans 是用function
# 非常的簡單 也容易閱讀
# 好像比較慢
    # 不知道是 test case 的問題  
    # 還是 function 呼叫比較慢的問題
class Solution:
    def countSubstrings(self, s: str):
        ans_count = 0
        
        def extendPalindromes(l,r) :
            nonlocal ans_count
            while l >= 0 and r < len(s) and s[l] == s[r] :
                ans_count += 1 
                l -= 1
                r += 1
        
        for i in range(len(s)) :
            extendPalindromes(i,i)
            extendPalindromes(i,i+1) #不用特別處理 因為會超出範圍 

        return ans_count

s = Solution()
print(s.countSubstrings())



