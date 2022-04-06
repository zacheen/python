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



