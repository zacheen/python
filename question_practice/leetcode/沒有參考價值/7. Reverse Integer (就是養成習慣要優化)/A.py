# my Runtime: 29 ms, faster than 94.80% of Python3
class Solution:
    def reverse(self, x: int):
        x_s = str(x)
        if x_s[0] == "-" :
            # fast
            if len(x_s) > 11:
                return 0
            ret = -int("".join(reversed(x_s[1:])))
        else :
            # fast
            if len(x_s) > 10:
                return 0
            ret = int("".join(reversed(x_s)))
            
        max_b = 2**31
        min_b = -max_b
        max_b = max_b-1
        if ret > max_b or ret < min_b :
            return 0
        else :
            return ret

# given ans 就是實作方法不一樣

s = Solution()
print(s.reverse(1123))



