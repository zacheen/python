# my Runtime: 35 ms, faster than 72.13% of Python3
class Solution:
    def climbStairs(self, n):
        mem = [0,1,2]
        
        # 我可以選擇走到第n-1格  或是走到第n-2格
        for n in range(3, n+1):
            mem.append( mem[n-1] + mem[n-2] )
             
        return mem[n]

# given ans 一樣

s = Solution()
print(s.climbStairs(3))



