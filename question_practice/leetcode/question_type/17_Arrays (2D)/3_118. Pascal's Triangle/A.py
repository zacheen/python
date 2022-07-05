# my Runtime: 42 ms, faster than 51.22% of Python3
class Solution:
    def generate(self, numRows):
        
        mem = [1]
        ans = [[1]]
        for i in range(2,numRows+1) : # base 0
            this_level = []
            last_level = ans[i-2]
            for ii in range(i):
                if (ii-1) < 0 :
                    left = 0
                else :
                    left = last_level[ii-1]
                    
                if (ii) >= len(last_level) :
                    right = 0
                else :
                    right = last_level[ii]
                    
                this_level.append(left+right)
                
            ans.append(this_level)
            
        return ans
                    
# given ans 
# 沒有比較快 但是比較好看
class Solution:
    def generate(self, numRows):
        ans = []

        for i in range(numRows):
            ans.append([1] * (i + 1))

        for i in range(2, numRows):
            for j in range(1, len(ans[i]) - 1):
                ans[i][j] = ans[i - 1][j - 1] + ans[i - 1][j]

        return ans

s = Solution()
print(s.generate(5))