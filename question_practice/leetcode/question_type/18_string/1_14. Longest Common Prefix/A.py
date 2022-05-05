# my Runtime: 38 ms, faster than 77.33% of Python3
class Solution:
    def longestCommonPrefix(self, strs):
        l = None
        all_fit = True
        for indx,c in enumerate(strs[0]) :
            l = indx
            fail = False
            for s in strs :
                if indx == len(s) or s[indx] != c :
                    fail = True
                    all_fit = False
                    break
            if fail :
                break
                
        if all_fit :
            return strs[0]
        else :
            return strs[0][:indx]

# given ans
# 概念一樣 只要其實break的地方就可以return
class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''

        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != strs[0][i]:
                    return strs[0][:i]

        return strs[0]
s = Solution()
print(s.longestCommonPrefix(["dog","dogg"]))
print(s.longestCommonPrefix(["dogg","dog"]))



