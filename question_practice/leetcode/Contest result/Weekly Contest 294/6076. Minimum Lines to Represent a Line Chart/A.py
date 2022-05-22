# my 
class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        if len(stockPrices) <= 1 :
            return 0
        
        
        stockPrices.sort()
        # print(stockPrices)
        
        def cal_slope(p1, p2) :
            return (p2[1]-p1[1])/(p2[0]-p1[0]) # All dayi are distinct. 所以不會除0
            
        last_slope = cal_slope( stockPrices[0] , stockPrices[1] )
        ans_count = 1
        for i in range(len(stockPrices)-1) :
            ret = cal_slope( stockPrices[i] , stockPrices[i+1] )
            if ret != last_slope :
                last_slope = ret
                ans_count += 1
        return ans_count
    
        # 我不知道 [[1,7],[2,6],[3,5],[4,4],[5,4],[6,2],[7,1],[8,0]] 這種定義算4或5條

# given ans

s = Solution()
print(s.())



