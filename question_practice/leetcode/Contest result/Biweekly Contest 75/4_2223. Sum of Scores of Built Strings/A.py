# 這有一個特殊的演算法 Z Algorithm

# my 是對的 但一開始超過 time limit 
# 是我強制加了優化的判斷才過的
# class Solution:
#     def sumScores(self, s: str) -> int:
#         score = 0
#         for i in range(len(s)) :
#             if s[-i] == s[0] :
#                 new_str = s[(-i):]
#                 # print(new_str, s[:i])
#                 if new_str == s[:i] :
#                     # print("fast")
#                     score += i
#                 else :
#                     for indx, e_s in enumerate(new_str) :
#                         if e_s == s[indx] :
#                             score += 1
#                         else :
#                             break
#             # print(now_str)
#         return score


# given ans
class Solution:
    def sumScores(self, s: str) -> int:
        def LcpByZ(target):
            len_t = len(target)
            lcp = [-1]*len_t
            top = 1
            right = 0
            lcp[0] = 0
            while top < len_t:
                while top+right < len_t and target[right] == target[top+right]:
                    right += 1
                lcp[top] = right
                left = 1
                if right == 0:
                    top += 1
                    continue
                while left+lcp[left] < right and left < right:
                    lcp[top+left] = lcp[left]
                    left += 1
                top += left
                right -= left
            return lcp

        lcp = LcpByZ(s)
        return sum(lcp)+len(s)

# Z Algorithm
class Solution:
    def sumScores(self, S):
        # https://github.com/cheran-senthil/PyRival/blob/master/pyrival/strings/z_algorithm.py
        # https://cp-algorithms.com/string/z-function.html
        n = len(S)
        Z = [0] * n
        l = r = 0

        for i in range(1, n):
            print(l , r)
            z = Z[i - l]
            if i + z >= r:
                z = max(r - i, 0)
                while i + z < n and S[z] == S[i + z]:
                    z += 1
                l, r = i, i + z
            Z[i] = z
            print(Z)

        Z[0] = n
        return sum(Z)

s = Solution()
# print(s.sumScores("babab"))
print(s.sumScores("azbazbzaz"))



