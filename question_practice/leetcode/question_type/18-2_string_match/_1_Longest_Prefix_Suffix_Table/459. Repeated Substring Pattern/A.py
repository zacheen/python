# 459. Repeated Substring Pattern
# https://leetcode.com/problems/repeated-substring-pattern/description/

# my using template cal_LPST : 35ms Beats30.22%
def cal_LPST(s): 
    len_s = len(s)
    lps = [0] * len_s
    pref_l = 0
    i = 1
    while i < len_s:
        if s[i] == s[pref_l]: # two pointer are the same word
            pref_l += 1
            lps[i] = pref_l
            i += 1
        else: # two pointer are not the same word
            if pref_l != 0: # find fast forward position
                pref_l = lps[pref_l - 1]
            else: # no fast forward position
                lps[i] = 0
                i += 1
    return lps

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        suffix_len = cal_LPST(s)[-1]
        if suffix_len == 0 :
            return False
        pre_l = len(s) - suffix_len
        if suffix_len%pre_l == 0:
            return True
        else :
            return False

# my using template Z-algorithm : 143ms Beats8.76%
def LCP(arr) :
    len_arr = len(arr)
    z = [0]*len_arr
    z_box_l = z_box_r = 0
    for i in range(1, len_arr):
        same_len = 0
        if i <= z_box_r :
            same_len = min(z_box_r-i+1, z[i-z_box_l])
                # z_box_r-i+1  : 如果 i~z_box_r 全部都一樣，長度會是多少
                # z[i-z_box_l] :  為了排除情況 "aabab"
            # if same_len > 0 : print("fast forward") # 應該要大於1 才會 fast forward
        while i + same_len < len_arr and arr[same_len] == arr[i+same_len]:
            # 這裡順序不能錯
            z_box_l = i
            z_box_r = i + same_len
            same_len += 1
        z[i] = same_len
    return z

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        lcp = LCP(s)
        for i, l in enumerate(lcp):
            if i+l == len(s) and l%i == 0:
                return True
        return False

# 從前面開始加 stack 
# 如果遇到相同的字母 先判斷是否能整除 再進 def 判斷
# My Runtime: 96 ms, faster than 53.21% of Python3 
class Solution:
    def repeatedSubstringPattern(self, s):
        def check_repeat(rep):
            # ------------------------------
            # 方法1
            # idx = len(rep)
            # while idx < len(s) :
            #     if s[idx:idx+len(rep)] != rep :
            #         return False
            #     idx += len(rep)
            # return True
            # ------------------------------
            # 方法2
            res = s.split(rep)
            if "".join(res) == "":
                return True
            else:
                return False
            # ------------------------------

        for i in range(1,len(s)//2+1) :
            repeat = s[:i]
            if s[i] == repeat[0] :
                if len(s) % len(repeat) == 0 :
                    if check_repeat(repeat) :
                        return True
        return False

# given ans 
# 邏輯是 再加上一次自己一定也會重複
# 所以除了原本的字串([1:-1]) 如果能夠找到原本的字串 一定是重複的字串                 
# class Solution:
#     def repeatedSubstringPattern(self, s):  
#         return s in (s + s)[1:-1]

s = Solution()
# print(s.repeatedSubstringPattern("ababab"))
print(s.repeatedSubstringPattern("aaaaaa"))
# print(s.repeatedSubstringPattern("abcdef"*30))
