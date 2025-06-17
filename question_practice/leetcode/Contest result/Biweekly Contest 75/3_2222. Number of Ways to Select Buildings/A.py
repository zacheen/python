# 2222. Number of Ways to Select Buildings
# https://leetcode.com/problems/number-of-ways-to-select-buildings/

# given ans : 203ms
    # 直接為各個dp狀態命一個變數
class Solution:
    def numberOfWays(self, s: str) -> int:
        ways = 0
        one = zero = zero_one = one_zero = 0
        for c in s:
            if c == '0':
                zero += 1
                one_zero += one
                ways += zero_one
            else:
                one += 1    
                zero_one += zero 
                ways += one_zero
        return ways

# my optimized by given ans : 985ms Beats18.53%
class Solution:
    def numberOfWays(self, s: str) -> int:
        dp = [[0,0,0] for _ in range(2)] # dp[type][remain]
        for c in s :
            if c == "0" :
                dp[0][0] +=1
                for i in range(1, 3) :
                    dp[0][i] += dp[1][i-1]
            else :
                dp[1][0] +=1
                for i in range(1, 3) :
                    dp[1][i] += dp[0][i-1]
        return dp[0][-1] + dp[1][-1]

# my practice again (for dp version)
class Solution:
    def numberOfWays(self, s: str) -> int:
        # for version
        dp = [[1,0,0,0] for _ in range(2)] # dp[type][remain]
        for c in s :
            if c == "0" :
                dp[0] = [1] + [c1+c2 for c1,c2 in zip(dp[1][:-1], dp[0][1:])]
            else :
                dp[1] = [1] + [c1+c2 for c1,c2 in zip(dp[0][:-1], dp[1][1:])]
        return dp[0][-1] + dp[1][-1]
        

        # recursive version would be Time Limit Exceeded
        # @cache
        # def dp(now_i, remain, prev_c):
        #     if remain == 0 :
        #         return 1
        #     if now_i == len(s):
        #         return 0
        #     ret = 0
        #     for new_st in range(now_i, len(s)) :
        #         if s[new_st] != prev_c :
        #             ret += dp(new_st+1, remain-1, s[new_st])
        #     return ret
        # return dp(0,3,"-")

# given ans
# 通用 template
class Solution:
    def numberOfWays(self, s: str):
        def F(s, t):
            f = [0] * (len(t) + 1)
            f[0] = 1
            for i in s:
                for j in range(len(t))[::-1]:
                    if t[j] == i: # 頭尾都是0或1
                        f[j + 1] += f[j]
                    print("f", f, i, -j)
            return f[len(t)]
        return F(s, '101') + F(s, '010')

# given ans (比較好看懂)
# 為特別案例 獨自優化
# class Solution:
#     def numberOfWays(self, s: str):
#         def f(t) :
#             a,b,c = 0,0,0
#             for x in s :
#                 print(a,b,c)
#                 if x == t[2] : c+=b  # 到目前這個x的位置 前面總共有幾個t[0]*t[1]*t[2]
#                 if x == t[1] : b+=a  # 到目前這個x的位置 前面總共有幾個t[0]*t[1]
#                 if x == t[0] : a+=1  # 到目前這個x的位置 前面總共有幾個t[0]
#             print("end :",a,b,c)
#             return c
#         return f("101") + f("010")

s = Solution()
# print(s.numberOfWays(s = "001101"))
print(s.numberOfWays(s = "1001"))



