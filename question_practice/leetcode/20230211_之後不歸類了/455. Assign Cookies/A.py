# My practice again : 15ms Beats93.50%
class Solution:
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        g_i = 0
        for s_n in s :
            if s_n >= g[g_i] :
                g_i += 1
                if g_i == len(g) :
                    break
        return g_i

# 思考 
# 1345
# 1245
# 最後分配 1 -> 1, 4 -> 3, 5 -> 4, 
# 最後分配 1 -> 1, 4 -> 4, 5 -> 5, 
# 這個時候這兩種分配方法的效益都是一樣的
# 因為滿足的人數一樣
# 所以解法才這麼簡單
# 如果 加起來 滿足感最大 就不一樣了

s = Solution()
print(s.findContentChildren([1,3,4,5],[1,2,4,5]))

