# my v1
class Solution:
    def minimumLines(self, stockPrices):
        if len(stockPrices) <= 1 :
            return 0
        
        stockPrices.sort()
        # print(stockPrices)
        
        # 不能直接比較 float 因為不精準
        def cal_slope(p1, p2) :
            print(p2[1]-p1[1], p2[0]-p1[0], (p2[1]-p1[1])/(p2[0]-p1[0]))
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
        # 算5條 所以問題不是在這裡

# 看 testcase 錯哪裡 去修改
# 當時有測試小數點 但沒測試到這麼極端
class Solution:
    def minimumLines(self, stockPrices):
        if len(stockPrices) <= 1 :
            return 0
        stockPrices.sort()
        def have_angle(p1, p2, p3) :
            diff_x1 = p2[0] - p1[0]
            diff_y1 = p2[1] - p1[1]
            diff_x2 = p3[0] - p2[0]
            diff_y2 = p3[1] - p2[1]
            
            # 要判斷 (diff_y1/diff_x1) == (diff_y2/diff_x2) -> diff_y1 * diff_x2 == diff_x1 * diff_y2
            # print(diff_y1 * diff_x2 , diff_x1 * diff_y2)
            return diff_y1 * diff_x2 != diff_x1 * diff_y2
            
        # 計算有幾個轉折
        ans_count = 1
        for i in range(len(stockPrices)-2) :
            if have_angle(stockPrices[i], stockPrices[i+1], stockPrices[i+2]) :
                ans_count += 1
            
        return ans_count

s = Solution()
print(s.minimumLines([[1,1],[500000000,499999999],[1000000000,999999998]]))



