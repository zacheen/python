# my Runtime: 981 ms, faster than 75.00% of Python3
class Solution:
    def minimumRounds(self, tasks):
        c = Counter(tasks)
        
        ans = 0
        for i,num in c.items():
            if num == 1 :
                return -1
            ans += (num+2)//3
            # 看 given ans 優化 原本 : ans += (num-1)//3 +1 
        return ans

# given ans 一樣

s = Solution()
print(s.minimumRounds(tasks = [2,2,3,3,2,4,4,4,4,4]))
print(s.minimumRounds(tasks = [2,3,3]))



