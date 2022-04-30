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
                    
s = Solution()
print(s.generate(5))