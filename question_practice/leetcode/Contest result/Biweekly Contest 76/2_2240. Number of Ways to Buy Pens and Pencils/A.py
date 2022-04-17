# my Runtime: 593 ms, faster than 100.00% of Python3
class Solution:
    def waysToBuyPensPencils(self, total, cost1, cost2):
        ans = 0
        for remain in range(total, -1, -cost1):
            ans += remain//cost2 + 1
        return ans
            
# given ans 我的寫法比較好

s = Solution()
print(s.waysToBuyPensPencils(total = 20, cost1 = 10, cost2 = 5)) # 9
print(s.waysToBuyPensPencils(total = 5, cost1 = 10, cost2 = 10)) # 1



